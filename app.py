import streamlit as st
from code_explainer import explain_code

st.set_page_config(page_title="🧠 AI Code Explainer", layout="wide")

st.title("🧠 AI Code Explainer (Offline using GPT4All)")
st.write("Paste your code below and get a beginner-friendly explanation.")

# Input area
code = st.text_area("💻 Enter your code snippet:", height=300, placeholder="Type or paste your Python/JavaScript code here...")

# Language dropdown
language = st.selectbox("🧪 Select code language", ["Python", "JavaScript", "C++", "Java", "Other"])

# Button
if st.button("🔍 Explain Code"):
    if not code.strip():
        st.warning("⚠️ Please paste some code to explain.")
    else:
        with st.spinner("🧠 Analyzing code..."):
            explanation = explain_code(code, language)
        st.subheader("📖 Explanation")
        st.success(explanation)
