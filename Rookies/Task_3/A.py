while True:
    X , Y =map(int,input().split())
    if X < 0 or Y > 100000:
       print("Try again")
       continue
    else:
       break
Sum = X+Y
print(Sum)   