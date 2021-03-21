from p3 import *
from sentiment_analysis import *
from summary import *
from newspaper import Article
from wc import *


def m2():
    activities = ["URL", "Text"]
    choice = st.selectbox("Select Text/URL", activities)

    if choice == 'URL':
        if choice:
            url = st.text_input('Input your URL here(Make sure there is no subscription attached:')
            if url:
                article = Article(url)
                article.download()
                article.parse()
                if st.button('wordcloud'):
                    wc(article.text)
                st.text("(WordCloud: Find most frequently used words)")
                sentiment_analysis(article.text)
                summary_code(article.text)

    if choice == 'Text':
        tx = st.text_area('Input your sentence here:')
        if st.button("Summarize"):
            if st.button('wordcloud'):
                wc(tx)
            st.text("(WordCloud: Find most frequently used words)")
            summary_code(tx)
            sentiment_analysis(tx)


