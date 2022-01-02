import re,shutil,os

fileRegex = re.compile(r"(TXT\s).*.txt$")
files = []
for filename in os.listdir("/home/gaurav02/Desktop/testing"):

    txtFile = fileRegex.search(f"/home/gaurav02/Desktop/testing{filename}")
    
    if txtFile == None:
        continue
    txtFile = txtFile.group()
    files.append(txtFile)

files.sort()
numRegex = re.compile(r"\d+")
counter = 1
print(files)
for i in files:
    txtnum = numRegex.search(i)
    txtnum = txtnum.group()
    print(txtnum)
    if int(txtnum) == counter:
        counter +=1
    else :
        print(counter)
        for i in range(counter, len(files)+1):
            shutil.move(
                f"/home/gaurav02/Desktop/testing/TXT {i+1}.txt", f"/home/gaurav02/Desktop/testing/TXT {i}.txt")
        break
