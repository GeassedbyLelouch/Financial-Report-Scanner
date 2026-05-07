import fitz
import streamlit as st

uploaded_file = st.file_uploader(
  label = "Upload a financial report",
  type = ["pdf"],
  help = "Please only upload pdf files"
)
total = ""
if uploaded_file is not None:
  file_bytes = uploaded_file.read()
  finished_file = fitz.open(stream=file_bytes, filetype="pdf")
  for page_number in range(len(finished_file)):
    page = finished_file[page_number]
    text = page.get_text()
    for line in text.split('\n'):
      if(line.strip().isdigit()):
        total+=line  

st.text_area("Extracted Text", total, height = 600, width = 1100)
  


 
