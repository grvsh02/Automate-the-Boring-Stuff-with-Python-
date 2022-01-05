import ezsheets

sheetObj = ezsheets.Spreadsheet("testing")
sheet = sheetObj[0]

emails = sheet.getColumn(3)
for i in emails:
    if i == "":
        break
    print(i)
