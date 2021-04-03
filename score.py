import textstat
import streamlit as st


def score(full):
    st.header(textstat.flesch_reading_ease(full))
    st.write('Flesch Reading Ease Score')
    text = """90-100 Very Easy,70-79 Fairly Easy,60-69 Standard,50-59Fairly Difficult,30-49 Difficult,0-29 Very 
    Confusing """
    st.write(text,key=1)

    st.header(textstat.smog_index(full))
    st.write('Smog Index Score')
    text = "Returns the SMOG index of the given text.This is a grade formula in that a score of 9.3 means that a ninth " \
           "grader would be able to read the document.Texts of fewer than 30 sentences are statistically invalid, " \
           "because the SMOG formula was normed on 30-sentence samples. textstat requires at least 3 sentences for a " \
           "result. "
    st.write(text,key=2)

    st.header(textstat.dale_chall_readability_score(full))
    st.write('Dale Chall Readability Score')
    text = """Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. 
            Thus it returns the grade level using the New Dale-Chall Formula.
            4.9 or lower	average 4th-grade student or lower
            5.0–5.9	average 5th or 6th-grade student
            6.0–6.9	average 7th or 8th-grade student
            7.0–7.9	average 9th or 10th-grade student
            8.0–8.9	average 11th or 12th-grade student
            9.0–9.9	average 13th to 15th-grade (college) student"""
    st.write(text,key=3)
