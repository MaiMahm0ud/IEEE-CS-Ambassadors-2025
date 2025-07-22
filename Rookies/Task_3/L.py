while True:
    N =int(input())
    if 1 <= N <= 1000:
       break
    else:
       print("Try again")
while True:
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) != N or len(B) != N:
        print(f"Please enter exactly {N} numbers")
        continue
    elif any(a < 1 or a > 100000 for a in A) or any(b < 1 or b > 100000 for b in B):
        print("invalid input")
        continue
    else:
        break
def new_array(a_list,b_list):
    C = b_list + a_list
    print(*C)
new_array(A,B)