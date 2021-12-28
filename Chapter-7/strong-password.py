import re

#dd/mm/yyyy

lengthRegex = re.compile(
r'\w{8,}'
)
upperRegex = re.compile(
r'[A-Z]'
)
lowerRegex = re.compile(
r'[a-z]'
)
digitRegex = re.compile(
r'[0-9]'
)
s = input()
if lengthRegex.search(s) != None:
    if upperRegex.search(s) != None:
        if lowerRegex.search(s) != None:
            if digitRegex.search(s) != None:
                print("valid password")
            else:
                print("No digit")
        else:
            print("no lower case")
    else:
        print("no upper case")
else:
    print("length < 8")