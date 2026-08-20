import pdfplumber
import pandas as pd

# Path to the PDF file
pdf_path = "E:\python\900013169803871.pdf"
excel_path = "E:\python\900013169803871.xlsx"

# List to store table data
data = []

# Open the PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        # Extract tables from the page
        tables = page.extract_table()
        if tables:
            for row in tables:
                # Ignore empty or improperly parsed rows
                if any(row):
                    data.append(row)

# Convert to Pandas DataFrame
columns = ["Installment No", "Start Date", "Due Date", "Interest Rate (%)", "Days", 
           "Principal Amount", "Interest Amount", "Charge", "Installment Amount", "Outstanding Balance"]
df = pd.DataFrame(data, columns=columns)

# Save to Excel
df.to_excel(excel_path, index=False)

print(f"Data successfully extracted to {excel_path}")
