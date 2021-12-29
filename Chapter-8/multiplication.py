import random, time

result = []

for i in range(10):
    n1 = random.randint(0,9)
    n2 = random.randint(0,9)

    for j in range(3):
        start = time.time()
        print("")
        print(f"Q{i}. {n1} x {n2} =" , end=" ")
        try:
            ans = int(input())
            end = time.time()
            if int(end - start) > 8 :
                print("time exceeded")
                result.append(f"time limit exceeded, answer was {n1*n2}")
                break
        except:
            print("please enter a valid integer")
            print(3 - j - 1, "chances left")
            continue
        if ans == n1*n2:
            print("Correct!!")
            time.sleep(1)
            result.append("correct")
            break
        else:
            print("Wrong answer!!")
            print(3 - j - 1, "chances left")
    else:
        result.append(f"wrong answer, answer was {n1*n2}")

print("\nResults :  \n\n")
for i,respond in enumerate(result):
    print("A",i+1,":",respond)