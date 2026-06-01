import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

workbook.save("Sanchez_Database.xlsx")