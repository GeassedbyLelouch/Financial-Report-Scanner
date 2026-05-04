import fitz
import streamlit as st

uploaded_file = st.file_uploader(
  label = "Upload a financial report",
  type = ["pdf"],
  accept_multiple_files =True,
  help = "Please only upload pdf files"
)
for page_number in range(len(doc)):
  page = doc[page_number]
  text = page.get_text()
  print(text)
 
