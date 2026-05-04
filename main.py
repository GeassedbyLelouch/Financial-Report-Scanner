import fitz
import streamlit as st

uploaded_file = st.file_uploader(
  label = "Upload a financial report",
  type = ["pdf"],
  help = "Please only upload pdf files"
)
finished_file = fitz.open(stream=uploaded_file.read(), filetype=pdf)

for page_number in range(len(finished_file)):
  page = finished_file[page_number]
  text = page.extract_text()
  st.text_area("Extracted Text", text)
 
