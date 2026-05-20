import streamlit as st
from transformers import pipeline

# Title and description
st.title("Sentiment Analysis Dashboard")
st.write("Upload text or type below to analyze sentiment using Hugging Face Transformers.")

# Load sentiment analysis pipeline
@st.cache_resource
def load_pipeline():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_pipeline()

# Text input
st.subheader("Enter Text")
user_input = st.text_area("Type your text here:")

# File upload
st.subheader("Upload a Text File")
uploaded_file = st.file_uploader("Choose a file", type=["txt"])

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input:
        # Analyze user input
        result = sentiment_pipeline(user_input)
        st.write("### Sentiment Analysis Result")
        st.json(result)
    elif uploaded_file:
        # Analyze uploaded file
        content = uploaded_file.read().decode("utf-8")
        result = sentiment_pipeline(content)
        st.write("### Sentiment Analysis Result")
        st.json(result)
    else:
        st.warning("Please provide text input or upload a file.")

# Footer
st.write("---")
st.write("Built with ❤️ using Streamlit and Hugging Face Transformers.")