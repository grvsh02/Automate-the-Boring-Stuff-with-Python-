import openpyxl

n = int(input("enter the number of files: "))
wb = openpyxl.Workbook()
sheet = wb.active
name = ""
a = "A"

for i in range(n):

    file = input("enter file name without extension(.txt)")
    fileobj = open(f"Chapter-13/{file}.txt")
    line = 1
    name = name + file
    for j in fileobj.readlines():
        j = j[:-1] 
        sheet[f"{chr(ord(a)+i)}{line}"] = j
        line = line + 1

    fileobj.close()

wb.save(f"Chapter-13/{name}.xlsx")
