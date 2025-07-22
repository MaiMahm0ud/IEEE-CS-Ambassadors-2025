while True:
    N =int(input())
    if 1 <= N <= 10000:
       break
    else:
       print("Try again")
matrix = []
while True:
    A = list(map(float, input().split()))
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
        continue
    elif any(x < 1.0 or x > 1000.0 for x in A):
        print("invalid input")
        continue
    else:
        matrix.append(A)
        break
        
def average(a_list):
    sum_num = 0 
    for i in a_list:
        sum_num += i
    aver = sum_num / len(a_list)
    print(aver)
average(matrix[0])