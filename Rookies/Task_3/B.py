while True:
    N = int(input())
    if 1 <= N <= 1000:
        break
    else:
        print("Try again")
def numbers(n):
    for i in range(1, n+1):
        if i < n:
            print(i, end=' ')
        else:
            print(i)
numbers(N)