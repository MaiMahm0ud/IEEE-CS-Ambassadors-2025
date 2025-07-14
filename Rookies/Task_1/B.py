N = int(input())
A = list(map(int, input().split()))
x = int(input())
for i in range(N):
    if A[i] == x:
        print(i)
        break

else:
        print("-1")