while True:
    N =int(input())
    if 1 <= N <= 10000:
       break
    else:
       print("Try again")
matrix = []
while True:
    A = list(map(int, input().split()))
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
        continue
    elif any(x < 0 or x > 1000 for x in A):
        print("invalid input")
        continue
    else:
        matrix.append(A)
        break
def Shift_Zeros(a_list):
    for i in range(len(a_list)):
        if a_list[i] == 0:
            a_list.remove(a_list[i])
            a_list.append(0)
    print(*a_list)
Shift_Zeros(matrix[0])