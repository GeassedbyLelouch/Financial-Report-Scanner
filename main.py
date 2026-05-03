import fitz

pdf_path = r"C:\Users\TronM\Documents\AJ\Apple_2025_10-K.pdf"
doc = fitz.open(pdf_path)
for(int page_number = 0; page_number + 1 == len(doc); page_number++){
  
page = doc[page_number]
text = page.get_text()

print(text)
}
