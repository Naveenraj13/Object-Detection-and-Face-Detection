from openpyxl import load_workbook

data_file = 'data/students.xlsx'
wb = load_workbook(data_file)

ws = wb['Sheet1']
all_rows = list(ws.rows)

for cell in all_rows[0]:
    print(cell.value)