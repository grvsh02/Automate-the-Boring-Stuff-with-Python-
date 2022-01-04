import openpyxl

file = input("enter file name without extension(.xlsx)")

wb = openpyxl.load_workbook(f"Chapter-13/{file}.xlsx")
sheet = wb.active
max_col = sheet.max_column

a = "A"
for i in range(max_col):

    txtFile = open(f"Chapter-13/TXT{i}.txt","w")
    line = 1

    while True:
        if sheet[f"{chr(ord(a)+i)}{line}"].value != None:

            txtFile.write(sheet[f"{chr(ord(a)+i)}{line}"].value)
            txtFile.write("\n")
            line = line + 1
        else:
            break
    txtFile.close()

wb.close
