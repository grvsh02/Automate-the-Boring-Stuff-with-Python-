import re,os,shutil

txtRegex = re.compile(r".*.txt$")

for folder, subfolder, filename in os.walk('/home/gaurav02/Desktop/testing'):
    for file in filename:
        txtFile = txtRegex.search(file)
        if txtFile == None:
            continue
        txtFile = txtFile.group()
        shutil.copy(
            f'/home/gaurav02/Desktop/testing/{txtFile}', f'/home/gaurav02/Desktop/copy')
