import streamlit as st
from pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="StudyMate AI", layout="centered")

st.title("📘 StudyMate AI - Smart Notes Generator")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    st.info("Processing your file...")
    text = extract_text_from_pdf(uploaded_file)
    
    st.subheader("📄 Extracted Text Preview:")
    st.text_area("Text from PDF", text, height=300)
