import streamlit as st
from textblob import TextBlob

st.title("AI-Based Sentiment Analyzer")

text = st.text_area("Enter your text here")

if st.button("Analyze Sentiment"):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    st.write("Polarity Score:", polarity)

    if polarity > 0:
        st.success("Positive 😊")

    elif polarity < 0:
        st.error("Negative 😞")

    else:
        st.info("Neutral 😐")