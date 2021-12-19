def writer(l):
    for index, item in enumerate(l):
        if index == len(l) - 1:
            print("and" , item)
        else:
            print(item + ',', end = " ")


l = list(input().split())
writer(l)