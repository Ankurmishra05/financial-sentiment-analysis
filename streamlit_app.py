import streamlit as st
import requests

API_URL = "https://financial-sentiment-analysis-qvt1.onrender.com"

st.set_page_config(layout="wide")

# ----------- SIDEBAR (LEFT PANEL) -----------
st.sidebar.title("📊 Settings")

st.sidebar.markdown("### Select Options")

num_news = st.sidebar.slider("Number of headlines", 1, 10, 5)

refresh = st.sidebar.button("🔄 Refresh Data")

# ----------- MAIN TITLE -----------
st.markdown("""
<h1 style='text-align: center; color: white;'>📈 Financial Dashboard</h1>
""", unsafe_allow_html=True)

# ----------- FETCH DATA -----------
if refresh:
    with st.spinner("Loading data..."):
        response = requests.get(f"{API_URL}/live-news")
        data = response.json()[:num_news]

        st.markdown("---")

        # ----------- DISPLAY CARDS -----------
        for item in data:
            sentiment = item["sentiment"]
            action = item["action"]

            # color logic
            if sentiment == "positive":
                color = "#22c55e"
            elif sentiment == "negative":
                color = "#ef4444"
            else:
                color = "#eab308"

            st.markdown(f"""
            <div style="
                background-color:#1e293b;
                padding:20px;
                border-radius:15px;
                margin-bottom:15px;
            ">
                <h3 style="color:white;">📰 {item['headline']}</h3>
                <p style="color:{color}; font-size:18px;">
                    Sentiment: {sentiment.upper()}
                </p>
                <p style="color:white;">
                    Action: <b>{action}</b>
                </p>
            </div>
            """, unsafe_allow_html=True)

# ----------- MANUAL INPUT -----------
st.markdown("## 🔍 Analyze Custom Headline")

headline = st.text_input("Enter headline")

if st.button("Analyze"):
    response = requests.post(f"{API_URL}/predict", json={"headline": headline})
    result = response.json()

    st.write(result)