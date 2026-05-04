import fitz
import streamlit as st

uploaded_file = st.file_uploader(
  label = "Upload a financial report",
  type = ["pdf"],
  accept_multiple_files =True,
  help = "Please only upload pdf files"
)
for page_number in range(len(uploaded_file)):
  page = uploaded_file[page_number]
  text = page.extract_text()
  st.text_area("Extracted Text", text)
 
