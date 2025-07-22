while True:
    X , N =map(int,input().split())
    if X < 0 or N > 10:
       print("Try again")
       continue
    else:
       break
def sum_num(m,n):
    S = 0
    for i in range(2,n+1):
        if i%2 == 0:
            S += (m**i)
    print(S)
sum_num(X,N)