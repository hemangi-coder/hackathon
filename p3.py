from fuzzywuzzy import fuzz
import numpy as np
import pandas as pd


# fuzzywuzzy code
def find_partitions(df, match_func, max_size=None, block_by=None):
    """Recursive algorithm for finding duplicates in a DataFrame."""

    # If block_by is provided, then we apply the algorithm to each block and
    # stitch the results back together
    if block_by is not None:
        blocks = df.groupby(block_by).apply(lambda g: find_partitions(
            df=g,
            match_func=match_func,
            max_size=max_size
        ))

        keys = blocks.index.unique(block_by)
        for a, b in zip(keys[:-1], keys[1:]):
            blocks.loc[b, :] += blocks.loc[a].iloc[-1] + 1

        return blocks.reset_index(block_by, drop=True)

    def get_record_index(r):
        return r[df.index.name or 'index']

    # Records are easier to work with than a DataFrame
    records = df.to_records()

    # This is where we store each partition
    partitions = []

    def find_partition(at=0, partition=None, indexes=None):

        r1 = records[at]

        if partition is None:
            partition = {get_record_index(r1)}
            indexes = [at]

        # Stop if enough duplicates have been found
        if max_size is not None and len(partition) == max_size:
            return partition, indexes

        for i, r2 in enumerate(records):

            if get_record_index(r2) in partition or i == at:
                continue

            if match_func(r1, r2):
                partition.add(get_record_index(r2))
                indexes.append(i)
                find_partition(at=i, partition=partition, indexes=indexes)

        return partition, indexes

    while len(records) > 0:
        partition, indexes = find_partition()
        partitions.append(partition)
        records = np.delete(records, indexes)

    return pd.Series({
        idx: partition_id
        for partition_id, idxs in enumerate(partitions)
        for idx in idxs
    })


def title(r1, r2):
    return r1['Headline'], r2['Headline']


def title_url(r1, r2):
    return r1['URL'], r2['URL']


def date(r1, r2):
    return r1['Date'] == r2['Date']


def same_title(r1, r2):
    return (
            fuzz.ratio(r1['Headline'], r2['Headline']) > 75 or
            fuzz.partial_ratio(r1['Headline'], r2['Headline']) > 80
    )


def same_title_url(r1, r2):
    return fuzz.partial_ratio(r1['URL'], r2['URL']) > 50


def same_news(r1, r2):
    return ((date(r1, r2) and same_title(r1, r2))
            or
            (same_title(r1, r2) and same_title_url(r1, r2)))
