N = int(input())
while True:
    if N < 1:
        print("Number must be 1 or greater Try again")
        N = int(input())
    else:
        break

while True:
    A = list(map(int, input().split()))
    
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
    elif any(x < 1 for x in A):
        print("not accepted Please try again")
    else:
        break 

rev = [A[i] for i in range(len(A)-1,-1,-1)]
if A == rev:
    print("YES")
else:
    print("NO")