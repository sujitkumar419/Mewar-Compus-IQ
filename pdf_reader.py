import fitz

doc = fitz.open("sample.pdf")

print("Total pages:", len(doc))