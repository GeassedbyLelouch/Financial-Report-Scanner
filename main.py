import fitz

pdf_path = r"C:\Users\TronM\Documents\AJ\Apple_2025_10-K.pdf"
doc = fitz.open(pdf_path)
page = doc[0]
text = page.get_text()

print(text[:500])
