import re
import os

regex = input()
searchRegex = re.compile(regex)
for i in os.listdir("/home/gaurav02/Desktop/Automate-the-Boring-Stuff-with-Python-/Chapter-9"):
    if i.endswith(".txt"):
        fileObj = open(
            f"/home/gaurav02/Desktop/Automate-the-Boring-Stuff-with-Python-/Chapter-9/{i}")
        contents = fileObj.read()
        results = searchRegex.search(contents)
        print(results)
