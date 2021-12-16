import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    l = []
    for i in range(100):
        
        if random.randint(0,1) == 1:
            print("True")
            l.append("T")
        else:
            print("Head")
            l.append("H")

    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 1
    flag = l[0]
    for i in range(1,100):
        if count == 6:
            numberOfStreaks += 1
            print("ohh yeahhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        if l[i] == flag:
            print("hello")

            count = count + 1
        else:
            print("no")
            flag = l[i]
            count = 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))