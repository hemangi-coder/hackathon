import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from newspaper import Article
from download import *
from p3 import find_partitions, same_news
from sentiment_analysis import *
from summary import *
from wc import *
from score import *


def m1():
    st.title("Upload Your File")
    filename = st.file_uploader("Choose a file", type=['xlsx', 'csv'])
    delimiter_choice = st.selectbox("In case you uploaded a CSV file, "
                                    "how is your data delimited?", [';', ','])
    st.markdown("---")

    # Function that tries to read file as a csv
    # if selected file is not a csv file then it will load as an excel file

    def try_read_df(f):
        try:
            return pd.read_csv(f, sep=delimiter_choice)
        except:
            return pd.read_excel(f)

    if filename:
        a = try_read_df(filename)
        # **********************************************
        a['id'] = find_partitions(
            df=a,
            match_func=same_news
        )
        # **********************************************
        # count
        b = a.groupby(['id']).size().reset_index(name='count')

        z = pd.merge(a, b, on="id", how="outer")
        # **********************************************
        choices = z['Headline']
        search = st.text_input('Input your sentence here:')
        if search:
            x = process.extract(search, choices)

            df = pd.DataFrame(x, columns=['Headline', 'ratio', 'dist'])

            i = pd.merge(z, df).drop_duplicates(subset='URL')

            j = i[['id']].loc[i['ratio'] == max(i.ratio)]

            k = pd.merge(j, z)
            result = k[['Date', 'Headline', 'URL']].drop_duplicates(subset='URL')

            # *****************************************************************
            result['id'] = find_partitions(
                df=result,
                match_func=same_news
            )
            r = result.drop_duplicates(subset='id')
            #Result Display

            st.header(r['Headline'][0])
            st.markdown(r['URL'][0])
            st.write('Unique highly related news')
            st.write(r)
            st.write('Search result with highest strength')
            st.write(result)


            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(result, 'YOUR_DF.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)

            df = pd.read_csv ('C:\Users\heman\Downloads\export.csv')
            df.head()
            #scrapping new
            url = result['URL'][0]
            article = Article(url)
            article.download()
            article.parse()
            sentiment_analysis(article.text)

            if st.button('wordcloud'):
                wc(article.text)
            st.text("(WordCloud: Find most frequently used words)")

            #summary
            summary_code(article.text)




