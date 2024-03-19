import pdfplumber
import csv

pdf_path = 'pd.pdf'

with pdfplumber.open(pdf_path) as pdf:
    with open('table_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        for page in pdf.pages:
            tables = page.extract_tables()
            print(tables)

            for table in tables:
                for row in table:
                    csv_writer.writerow(row)

print("Tabular data extracted from PDF and written to table_data.csv successfully.")
