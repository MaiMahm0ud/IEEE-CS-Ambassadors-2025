N = int(input())
while True:
    if N < 2 or N > 1000:
        print("Number must be between 2 , 1000")
        N = int(input())
    else:
        break
A = list(map(int, input().split()))
min_num = A[0] 
x = 0
for i in range(N):
    if A[i] < min_num:
        min_num = A[i]
        x = i
print(min_num,(1+x))
