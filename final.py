import streamlit as st
from model3 import *
from model1 import *
from model2 import *


def main():
    """Summaryzer Streamlit App"""

    st.title("ABC Ez Summerizer")

    activities = ["Copy via URL/Text", "Upload news via CSV/xlxs","Fetch Live News"]
    choice = st.sidebar.selectbox("How do you wish to fetch the news ?", activities)

    if choice == 'Fetch Live News':
        m3()

    if choice == 'Upload news via CSV/xlxs':
        m1()

    if choice == 'Copy via URL/Text':
        m2()

    st.sidebar.header(" ")
    st.sidebar.header('')
    st.sidebar.header('')
    st.sidebar.header('')
    st.sidebar.header('')
    st.sidebar.header('')
    st.sidebar.header('GROUP 2')
    st.sidebar.write('Coded By: Hemangi Koli')
    st.sidebar.write('Designed & Assisted By:')
    st.sidebar.write('  Rahul Gaur')
    st.sidebar.write('  Nikitha Palle ')
    st.sidebar.write('  Anamika Raha')
    st.sidebar.write('  Sarvadnya Chabbi')
    st.sidebar.write('  Manikanta Chalagalla')

if __name__ == '__main__':
    main()
