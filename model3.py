from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import numpy as np
from newspaper import Article
from newsapi import NewsApiClient
import pandas as pd
from p3 import *
from download import *
from sentiment_analysis import *
from summary import *
from p3 import find_partitions, same_news
from wc import *


def m3():
    api = NewsApiClient(api_key='8262bbee87844df9b5924b3d49891260')
    search = st.text_input('Search Live news through keywords:')
    if search:
        data = api.get_everything(q=search)
        articles = data['articles']
        Date = []
        URL = []
        Headline = []
        for x, y in enumerate(articles):
            Date.append(y["publishedAt"])
            URL.append(y["url"])
            Headline.append(y["title"])
        df1 = pd.DataFrame(Date, columns=['Date'])
        df2 = pd.DataFrame(URL, columns=['URL'])
        df3 = pd.DataFrame(Headline, columns=['Headline'])
        df1['URL'] = df2['URL']
        df1['Headline'] = df3["Headline"]
        a = df1
        # **********************************************
        a['id'] = find_partitions(
            df=a,
            match_func=same_news
        )
        #
        # **********************************************
        # count
        b = a.groupby(['id']).size().reset_index(name='count')

        z = pd.merge(a, b, on="id", how="outer")
        # **********************************************
        choices = z['Headline']
        x = process.extract(search, choices)

        df = pd.DataFrame(x, columns=['Headline', 'ratio', 'dist'])

        i = pd.merge(z, df).drop_duplicates(subset='URL')

        j = i[['id']].loc[i['ratio'] == max(i.ratio)]

        k = pd.merge(j, z)
        z = k[['Date', 'Headline', 'URL']]
        result = k[['Date', 'Headline', 'URL']].drop_duplicates(subset='URL')
        # *****************************************************************
        result['id'] = find_partitions(
            df=result,
            match_func=same_news
        )
        r = result.drop_duplicates(subset='id')
        # Result display
        st.header(r['Headline'][0])
        st.markdown(r['URL'][0])
        st.write('Unique highly related news')
        st.write(r)
        st.write('Search result with highest strength')
        lt = a.drop(['id'], axis=1)
        st.write(a.drop(['id'], axis=1))

        if st.button('Download Dataframe as CSV'):
            tmp_download_link = download_link(lt, 'YOUR_DF.csv', 'Click here to download your data!')
            st.markdown(tmp_download_link, unsafe_allow_html=True)

        url = result['URL'][0]
        article = Article(url)
        article.download()
        article.parse()
        # wordcloud
        if st.button('wordcloud'):
            wc(article.text)
        st.text("(WordCloud: Find most frequently used words)")
        sentiment_analysis(article.text)

        # summary
        summary_code(article.text)
