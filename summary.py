import streamlit as st
# Sumy Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from score import *
import nltk
nltk.download('punkt')

# Lex Rank
def lex_rank(docx,x):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, x)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


# Luhn
def luhn(docx,x):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    summarizer_1 = LuhnSummarizer()
    summary = summarizer_1(parser.document, x)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


# LSA
def lsa(docx,x):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    summarizer_2 = LsaSummarizer()
    summary = summarizer_2(parser.document, x)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result


# LSA
def text_rank(docx,x):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    summarizer_3 = TextRankSummarizer()
    summary_3 = summarizer_3(parser.document, x)
    summary_list = [str(sentence) for sentence in summary_3]
    result = ' '.join(summary_list)
    return result


def summary_code(message):
    summary_options = st.selectbox("Choose Summarizer", ['Text Rank', 'Luhn', 'LSA', 'Lex Rank'])

    if summary_options == 'Lex Rank':
        search1 = st.number_input('Input desired no. of minutes for article read:', key=1,min_value=3)
        if search1:
            st.text("Using Lex Rank Summarizer ..")
            summary_result = lex_rank(message, search1)
            st.success(summary_result)
            if st.button('Quality Check'):
                score(message)
            st.write('(FOR NERDS ONLY-Use above Quality Check option to evaluate summary)')
    elif summary_options == 'Luhn':
        search2 = st.number_input('Input desired no. of minutes for article read:', key=2,min_value=3)
        if search2:
            st.text("Using Luhn Summarizer ..")
            summary_result = luhn(message, search2)
            st.success(summary_result)
            if st.button('Quality Check'):
                score(message)
            st.write('(FOR NERDS ONLY-Use above Quality Check option to evaluate summary)')
    elif summary_options == 'LSA':
        search3 = st.number_input('Input desired no. of minutes for article read:', key=3,min_value=3)
        if search3:
            st.text("Using LSA Summarizer ..")
            summary_result = lsa(message, search3)
            st.success(summary_result)
            if st.button('Quality Check'):
                score(message)
            st.write('(FOR NERDS ONLY-Use above Quality Check option to evaluate summary)')
    else:
        search4 = st.number_input('Input desired no. of minutes for article read:', key=4,min_value=3)
        if search4:
            st.text("Using Text Rank Summarizer ..")
            summary_result = text_rank(message, search4)
            st.success(summary_result)
            if st.button('Quality Check'):
                score(message)
            st.write('(FOR NERDS ONLY-Use above Quality Check option to evaluate summary)')
