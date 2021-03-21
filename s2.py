import pandas as pd
from s1 import *

news = pd.read_excel(r'C:\Users\heman\Downloads\shorya.xlsx')

news['real_id'] = find_partitions(
    df=news,
    match_func=same_news
)
##########################################################################################
##########################################################################################################
n1 = 'to'
result = news[news["Headlines"].str.contains(n1)]
print(result)