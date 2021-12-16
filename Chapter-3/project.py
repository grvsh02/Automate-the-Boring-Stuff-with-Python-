def collatz(n):
    if n % 2 == 0:
        ans = n//2
    else:
        ans = 3 * n + 1
    print(ans)
    return ans

try :

    num = int(input())
    ans = collatz(num)
    while ans != 1:
        ans = collatz(ans)

except ValueError:
    print("please enter a integer")


