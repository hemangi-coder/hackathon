import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Create some sample text
def wc(text):
    # Create and generate a word cloud image:
    wordcloud = WordCloud(background_color='white',max_words=20).generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # plt.show()
    st.pyplot()
