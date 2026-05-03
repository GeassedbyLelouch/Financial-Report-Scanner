import fitz

pdf_path = r"C:\Users\TronM\Documents\AJ\Apple_2025_10-K.pdf"
doc = fitz.open(pdf_path)
for page_number in range(len(doc)):
  page = doc[page_number]
  text = page.get_text()
  print(text)
  if page_number + 1 == len(doc):
    break
