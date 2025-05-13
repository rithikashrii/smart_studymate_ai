# 📄 smart_studymate_ai/main.py
# Main controller for Smart StudyMate AI
# Developed for CBSE Class 12 Board Project - Full-fledged application

import streamlit as st
import datetime
from pdf_reader import extract_text_from_pdf
from notes_generator import generate_detailed_notes
from hots_generator import generate_hots_questions

# Streamlit configuration
st.set_page_config(page_title="Smart StudyMate AI", layout="wide")

# Title and description
st.title("📘 Smart StudyMate AI")
st.caption("Developed as part of CBSE Class 12 Computer Science Project")
st.subheader("Upload any academic chapter PDF and get instant, exam-ready notes and HOTS questions")
st.markdown("""
### 💡 How it works:
1. Upload your chapter PDF (History, Biology, Business Studies — any subject)
2. The app extracts key content using AI-enhanced methods
3. It then generates:
    - ✍️ Bullet-style **Detailed Notes**
    - 🧠 Higher Order Thinking Skills (**HOTS**) Questions
4. Everything can be exported for revision
""")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your chapter PDF", type=["pdf"])

# Optional date and session tracking
today = datetime.date.today()
st.sidebar.markdown(f"**Session Date:** {today}")
st.sidebar.markdown("Developed by: Your Name")

# Main logic for processing the PDF
if uploaded_file is not None:
    with st.spinner("🔍 Reading and analyzing your PDF. Please wait..."):
        try:
            # Step 1: Extract raw text from PDF (fixing potential read issue)
            pdf_bytes = uploaded_file.read()
            pdf_text = extract_text_from_pdf(pdf_bytes)

            # Step 2: Generate detailed notes
            notes = generate_detailed_notes(pdf_text)

            # Step 3: Generate HOTS questions
            hots = generate_hots_questions(pdf_text)

            st.success("✅ Processing complete! Your notes and HOTS are ready.")

            # Output Section: Notes
            st.markdown("### 📚 Detailed Study Notes")
            st.text_area("Auto-Generated Notes", notes, height=400)

            # Output Section: HOTS Questions
            st.markdown("### 💡 HOTS (Higher Order Thinking Skills) Questions")
            hots_text = "\n".join([f"{i}. {q}" for i, q in enumerate(hots, 1)])
            st.text_area("HOTS Questions", hots_text, height=200)

            # Download options
            st.download_button("📥 Download Notes (TXT)", notes, file_name="study_notes.txt")
            st.download_button("📥 Download HOTS Questions (TXT)", hots_text, file_name="hots_questions.txt")

        except Exception as e:
            st.error("❌ An error occurred while processing the file.")
            st.exception(e)
else:
    st.info("⬆️ Please upload a PDF file to begin.")
