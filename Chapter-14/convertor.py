import ezsheets

s = input("please enter the name of the file :- ")

ss = ezsheets.upload(s)

ss.downloadAsExcel()
ss.downloadAsODS()
ss.downloadAsCSV()
ss.downloadAsTSV()
ss.downloadAsPDF()
ss.downloadAsHTML()
