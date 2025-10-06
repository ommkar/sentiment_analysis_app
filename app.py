import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

# User input
user_input = st.text_area("Enter text to analyze:", "Type something here...")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        blob = TextBlob(user_input)
        sentiment = blob.sentiment
        st.write(f"**Polarity:** {sentiment.polarity:.2f} (Range: -1.0 negative to 1.0 positive)")
        st.write(f"**Subjectivity:** {sentiment.subjectivity:.2f} (Range: 0.0 objective to 1.0 subjective)")
        
        if sentiment.polarity > 0.1:
            st.success("Positive!")
        elif sentiment.polarity < -0.1:
            st.error("Negative!")
        else:
            st.warning("Neutral")
    else:
        st.error("Please enter some text.")