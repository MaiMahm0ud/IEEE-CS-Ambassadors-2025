N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] > 0:
        A[i]= 1
    elif A[i] <0:
        A[i] = 2
print(*A)    