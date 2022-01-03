import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active

n = int(input())
boldFont = Font(bold = True)
a = 'A'
for i in range(1,n+1):
    sheet[f'A{i+1}'] = i
    sheet[f'A{i}'].font = boldFont
for i in range(1,n+1):
    sheet[f"{chr(ord(a)+i)}{1}"] = i
    sheet[f"{chr(ord(a)+i)}{1}"].font = boldFont

for i in range(1,n+1):
    for j in range(1,n+1):
        sheet[f"{chr(ord(a)+i)}{j+1}"] = i*j

wb.save("Chapter-13/table.xlsx")
