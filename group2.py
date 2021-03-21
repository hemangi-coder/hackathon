import streamlit as st
import pandas as pd
from p3 import fuzz
from p3 import process


# fuzzywuzzy
def fuzzywuzzy(query, choices):
    summary_list = process.extract(query, choices)
    return summary_list


def main():
    """ NLP Based App with Streamlit """
    df = pd.read_excel(r"C:\Users\heman\Downloads\Hackathon\Final excel.xlsx")
    choices = df['Headline']
    # Title
    st.title("Curation of newsfeeds")

    # Summarization
    if st.checkbox("De-duping of news items"):

        message = st.text_area("Enter Text", "Type Here ..")
        summary_options = st.selectbox("Choose De-duping Technique", ['Fuzzywuzzy', 'Levenshtein', 'Ngram'])
        if st.button("Analyze"):
            if summary_options == 'Fuzzywuzzy':
                st.text("Using Fuzzywuzzy ..")
                summary_result = fuzzywuzzy(message, choices)

            st.success(summary_result)


if __name__ == '__main__':
    main()
