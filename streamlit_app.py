import streamlit as st
from simple_sentiment_analyzer import SimpleSentimentAnalyzer

# Page config
st.set_page_config(page_title="Simple Sentiment Analyzer", page_icon="📊")

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    .stButton button {
        width: 100%;
        border-radius: 10px;
        background-color: #6366f1;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Simple Sentiment Analyzer")
st.write("Understand the emotion behind every word with precision.")

text_input = st.text_area("Enter text to analyze:", placeholder="I really enjoyed the evening...")

if st.button("Analyze Sentiment"):
    if text_input:
        blob = SimpleSentimentAnalyzer(text_input)
        sentiment = blob.sentiment
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Polarity", f"{sentiment.polarity:.2f}", help="(-1.0 to 1.0) Positive vs Negative")
            st.progress((sentiment.polarity + 1) / 2)
            
        with col2:
            st.metric("Subjectivity", f"{sentiment.subjectivity:.2f}", help="(0.0 to 1.0) Opinion vs Fact")
            st.progress(sentiment.subjectivity)
        
        # Result Badge
        if sentiment.polarity > 0.1:
            st.success("Result: Positive")
        elif sentiment.polarity < -0.1:
            st.error("Result: Negative")
        else:
            st.warning("Result: Neutral")
    else:
        st.warning("Please enter some text first.")
