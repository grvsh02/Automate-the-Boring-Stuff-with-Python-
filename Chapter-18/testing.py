import random
import ezgmail

email_file = input("please enter the files with all the emails :")

file = open(f"Chapter-18/{email_file}","r")
chores = ["make food","feed the fishes","take dog for a walk","wash dishes","pay bills","bring milk","clean house"]

for recipent in file.readlines():
    recipent = recipent[:-1]
    task = random.choice(chores)
    chores.remove(task)
    print("assigning",recipent,"with",task)
    ezgmail.send(recipent,"Your todays task",task)

if len(chores) > 0:
    print("\n\nwe still have the following tasks left: ")
    for i in chores:
        print(i)