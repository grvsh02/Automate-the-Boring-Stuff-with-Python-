import PyPDF2, os

pwd = input("please enter the encrytion password: ")
for folder, subfolder, filename in os.walk("Chapter-15"):

    for file in filename:

        if file.endswith(".pdf"):

            pdfFile = open(f"Chapter-15/{file}","rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            
            for page_num in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(page_num))

            file = file[:-4]

            pdfWriter.encrypt(pwd)
            encryptedPdf = open(f"Chapter-15/{file}_encrypted.pdf", "wb")
            pdfWriter.write(encryptedPdf)
            print(f"encryted {file} as {file}_encrypted.pdf")
            pdfFile.close()
            encryptedPdf.close()
