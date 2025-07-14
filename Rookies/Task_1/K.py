N = int(input())
while True:
    if N < 1:
        print("Number must be greater than 1")
        N = int(input())
    else:
        break

while True:
        A = input()
        if len(A) != N:
            print(f"Please enter exactly {N} numbers")
            continue 
        elif not A.isdigit():
            print("Input must contain digits only")
            continue
        A_ = list(map(int, A))
        break 
    
    
sum = 0
for i in range(N): 
    sum = sum + A_[i]
print(sum)
