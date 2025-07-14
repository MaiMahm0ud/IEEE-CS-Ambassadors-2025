N = int(input())
while True:
    if N < 2 or N > 1000:
        print("Number must be between 2,1000")
        N = int(input())
    else:
        break
while True:
    A = list(map(int, input().split()))
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
        continue 
    else:
        break
min_num = A[0]    
max_num = A[1]
for i in range(N):
    if A[i] < min_num:
        min_num = A[i]
    elif A[i] > max_num:
        max_num = A[i]
        
for i in range(N):
    if min_num == A[i]:
        x = i 
    elif max_num == A[i]:
        y = i 
A[x],A[y] = A[y],A[x]
print(*A)