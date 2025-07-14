N = int(input())
while True:
    if N <= 0:
        print("Number must be 1 or greater Try again")
        N = int(input())
    else:
        break

while True:
    A = list(map(int, input().split()))
    
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
    elif any(x < -100 or x >100 for x in A ):
        print("not accepted Please try again")
    else:
        break
    
for i in range(N):
    for j in range(0, N - i - 1):
        if A[j] > A[j + 1]:  
           A[j], A[j + 1] = A[j + 1], A[j]

print(*A)