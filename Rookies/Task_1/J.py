N = int(input())
while True:
    if N < 2 or N > 1000:
        print("Number must be between 2 , 1000")
        N = int(input())
    else:
        break

while True:
    A = list(map(int, input().split()))
    
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
    else:
        break
min_value = min(A)
count = A.count(min_value)


if count % 2 ==0 :
    print("Unlucky")
else:
    print("Lucky")
        