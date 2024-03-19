import pandas as pd
import tabula


def clean_table(table):
    for col in table:
        table[col] = [val if val != "P’000" else "" for val in table[col]]
    table = table.map(lambda x: '' if str(x) == 'nan' or str(x) == 'None' else x)
    return table

pdf_path = 'pd.pdf'

tables = tabula.read_pdf(pdf_path,   stream=True)

for i, table in enumerate(tables[:4]):
    cleaned_table = clean_table(table)


    output_csv_path = f'table_{i + 1}.csv'
    cleaned_table = cleaned_table.loc[:, ~cleaned_table.columns.str.startswith('Unnamed')]
    cleaned_table = pd.DataFrame(cleaned_table)
    cleaned_table.to_csv(output_csv_path, index=False)
