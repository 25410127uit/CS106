# app.py
import streamlit as st
from core import ai_recommend_algorithm, ai_grade_code

st.set_page_config(page_title="DSA AI Trainer", layout="centered")

st.title("🧠 Interactive DSA AI Trainer")

st.markdown(
    """
Enter a **problem description**, write your **Python solution**,
and let the AI suggest an approach and test your code.
"""
)

problem = st.text_area("📘 Problem description")
code = st.text_area("💻 Your Python code", height=220)

# demo test case
tests = [([1, 2, 3], 6)]

if st.button("🚀 Run AI"):
    if not problem or not code:
        st.warning("Please enter both problem description and code.")
    else:
        st.subheader("🔍 AI Recommendation")
        st.info(ai_recommend_algorithm(problem))

        st.subheader("🧪 Code Evaluation")
        ok, msg = ai_grade_code(code, tests)
        if ok:
            st.success(msg)
        else:
            st.error(msg)

st.caption("Educational use only • Sandbox execution")
