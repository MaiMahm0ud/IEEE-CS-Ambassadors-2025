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
    elif any(x < 0 or x > 100000 for x in A):
        print("invalid input")
        continue
    else:
        matrix.append(A)
        break
def max_min (a_list):
    min_num = a_list[0]    
    max_num = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] < min_num:
            min_num = a_list[i]
        elif a_list[i] > max_num:
            max_num = a_list[i]
    print(f"{min_num} {max_num}")   
max_min(matrix[0])