import re

def strip(string, char):
    if char == "":
        charRegex = re.compile(r'^\s+|\s+$')
        result = charRegex.sub("",string)
        return result
    else:
        charRegex = re.compile(f'^{char}+|{char}+$')
        result = charRegex.sub("", string)
        return result


c = input('character :')
s = input('string :')

print(strip(s, c))
