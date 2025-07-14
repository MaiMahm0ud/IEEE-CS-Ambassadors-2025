N = int(input())
if N < 2 :
    print("invalid input")
else:
    A = list(map(int, input().split()))
    found = False
    for i in range(N):
        if A[i] <= 10:
            print(f"A[{i}] = {A[i]}")
            found = True
    if not found:
        print("no numbers less than or equal to 10")