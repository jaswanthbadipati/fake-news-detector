import streamlit as st
from utils.news_fetcher import predict_news

# App Title
st.set_page_config(page_title="Real-Time Fake News Detector", layout="centered")
st.title("📰 Real-Time Fake News Detector")
st.write("Enter or paste a news article or statement below to check if it's **Real** or **Fake**.")

# Text Input Area
user_input = st.text_area("✍️ Input News Article", height=250, placeholder="Paste news content here...")

# Predict Button
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some news content.")
    else:
        with st.spinner("Analyzing..."):
            label, confidence = predict_news(user_input)
            st.success(f"🧠 Prediction: **{label}**")
            st.info(f"📊 Confidence: {confidence}%")

# Footer
st.markdown("---")
st.caption("Model by [jy46604790/Fake-News-Bert-Detect](https://huggingface.co/jy46604790/Fake-News-Bert-Detect)")
