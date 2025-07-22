while True:
    X,Y = map(int,input().split())
    if 0 <= X and Y <= 100000:
        break
    else:
        print("Try again")
def swap_num(a,b):
    a,b = b,a
    print(f"{a} {b}")

swap_num(X,Y)