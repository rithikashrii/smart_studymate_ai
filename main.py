# 📄 main.py
import streamlit as st
from pdf_reader import extract_text_from_pdf

# Streamlit page settings
st.set_page_config(page_title="Smart StudyMate AI", layout="centered")

# Title section
st.title("📘 Smart StudyMate AI")
st.caption("Your personal assistant to generate exam-ready notes and HOTS questions")
st.markdown("---")

# File upload section
uploaded_file = st.file_uploader("📤 Upload your chapter PDF", type=["pdf"])

# Process the PDF
if uploaded_file:
    st.success("✅ File uploaded successfully!")
    st.info("🔍 Extracting text from your PDF. Please wait...")

    try:
        extracted_text = extract_text_from_pdf(uploaded_file)

        st.markdown("### 📄 Extracted Text:")
        st.text_area("Here’s what we got from the PDF:", extracted_text, height=300)

        # Optional next step
        st.markdown("---")
        st.markdown("ℹ️ **Want to generate notes or HOTS next? Let me know to unlock that!**")

    except Exception as e:
        st.error("❌ An error occurred while reading the PDF.")
        st.exception(e)
else:
    st.warning("⬆️ Please upload a PDF file to begin.")
