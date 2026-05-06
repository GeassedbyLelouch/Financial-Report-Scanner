import fitz
import streamlit as st

uploaded_file = st.file_uploader(
  label = "Upload a financial report",
  type = ["pdf"],
  help = "Please only upload pdf files"
)
total = ""
if uploaded_file is not None:
  bytes = uploaded_file.read()
  finished_file = fitz.open(stream=bytes, filetype="pdf")
  for page_number in range(len(finished_file)):
    page = finished_file[page_number]
    text = page.get_text()
    total += text
else:
  print("Please upload a file")
st.text_area("Extracted Text", total)
  


 
