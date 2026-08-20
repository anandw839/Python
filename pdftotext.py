from PyPDF2 import PdfReader

reader = PdfReader("E:\\Resume\\Updated_Resume_Anand_Waghmare.pdf")

text = ""
for i, page in enumerate(reader.pages):
    text += f"\n--- Page {i+1} ---\n"
    text += page.extract_text()

with open("E:\\Resume\\output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Done!")