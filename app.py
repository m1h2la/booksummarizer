import streamlit as st
import requests

st.set_page_config(page_title="📘 Book Summary Web App", layout="centered")

st.title("📘 Book Summary Web App")

st.markdown("""
This app lets users:
- 📄 Upload a book file (PDF, DOCX, etc.)
- 📚 Summarize each chapter
- 🧠 Extract topic summaries from specific page ranges
- 🧾 Get the overall concept of the book
""")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload Book File (PDF, DOCX, etc):", type=["pdf", "doc", "docx"])

# --- Summary Type Options ---
summary_type = st.radio("Choose Action:", [
    "Chapter Summary", 
    "Topic Summary (with Page Range)", 
    "Book Concept"
])

# --- Page range for topic summary ---
start_page, end_page = None, None
if summary_type == "Topic Summary (with Page Range)":
    col1, col2 = st.columns(2)
    with col1:
        start_page = st.number_input("Start Page:", min_value=1, step=1)
    with col2:
        end_page = st.number_input("End Page:", min_value=1, step=1)

# --- Submission ---
if uploaded_file:
    st.success("✅ File uploaded successfully.")
    if st.button(f"Generate {summary_type}"):
        with st.spinner("⏳ Processing your file, please wait..."):
            try:
                files = {"file": uploaded_file}
                data = {"type": summary_type.lower().replace(" ", "")}

                if summary_type == "Topic Summary (with Page Range)":
                    data["start_page"] = int(start_page)
                    data["end_page"] = int(end_page)

                response = requests.post("http://localhost:8000/summarize", files=files, data=data)

                if response.status_code == 200:
                    result = response.json().get("result", "No summary found.")
                    st.text_area("📄 Result:", value=result, height=300)
                else:
                    st.error("❌ Failed to get summary. Please try again.")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
else:
    st.info("⬆️ Please upload a book file to begin.")
