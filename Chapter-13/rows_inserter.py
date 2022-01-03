import openpyxl

n,m = [int(x) for x in input().split()]
file = input()
wb = openpyxl.load_workbook(f"Chapter-13/{file}")
sheet = wb.active

sheet.insert_rows(n,m)
wb.save(f"Chapter-13/converted_{file}")
