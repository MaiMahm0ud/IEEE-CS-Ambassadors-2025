T = int(input())
while T < 1 or T > 100:
    T = int(input("Enter number of test cases: "))
    
for _ in range(T):
    N = int(input())
    while True:
        if N < 2:
            print("Number must be 2 or greater Try again")
            N = int(input())
        elif N > 100:
            print("Number must be between 2 , 100")
            N = int(input())
        else:
            break

    while True:
         A = list(map(int, input().split()))
    
         if len(A) != N:
             print(f"Please enter exactly {N} numbers")
         else:
            break
    min_result = float('inf')
    min_value = A[0] - 0 
  
    for j in range(1, N):
        current = A[j] + j + min_value
        min_result = min(min_result, current)
        min_value = min(min_value, A[j] - j)
        
    print(min_result)