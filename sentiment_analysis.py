import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from speedometer import *
import nltk
nltk.download('vader_lexicon')

def sentiment_analysis(message):
    sia = SIA()
    p_score = sia.polarity_scores(message)
    p = p_score['compound']
    speedometer(p)
