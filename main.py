import fitz

pdf_path = "./data/Apple_2025_10-K.pdf"
doc = fitz.open(pdf_path)
for page_number in range(len(doc)):
  page = doc[page_number]
  text = page.get_text()
  print(text)
 
