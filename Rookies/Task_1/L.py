T = int(input())
while True:
    if T < 1 or T > 5:
        print("Number must be between 1,5")
        T = int(input())
    else:
        break
for _ in range (T):
    N = int(input())
    while True:
        if N < 1 or N > 100:
            print("Number must be between 1,100")
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
    result = [] 
    for i in range(1, N + 1):
        for j in range(N - i + 1):
            sub = A[j:j + i]
            result.append(max(sub))

            
    print(*result)