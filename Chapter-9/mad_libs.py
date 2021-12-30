from os import WCOREDUMP


fileObj = open(
    '/home/gaurav02/Desktop/Automate-the-Boring-Stuff-with-Python-/Chapter-9/test.txt'
)
contents = fileObj.read()
fileObj.close()

l = list(contents.split(" "))
print(l)
for i,word in enumerate(l):
    if word == "ADJECTIVE":
        adj = input("Enter an adjective: ")
        l[i] = adj
    elif word == "NOUN":
        noun = input("Enter an noun ")
        l[i] = noun
    elif word == "ADVERB":
        adverb = input("Enter a adverb: ")
        l[i] = adverb
    elif word == "VERB":
        verb = input("Enter a verb: ")
        l[i] = verb

s = ""

for i in l:
    s = s + i + " "

fileObj = open(
    '/home/gaurav02/Desktop/Automate-the-Boring-Stuff-with-Python-/Chapter-9/test_update.txt',"w"
)

fileObj.write(s)
fileObj.close()