while True:
    T = int(input())
    if 1 <= T <= 1000:
        break
    else:
        print("Try again")
for _ in range(T):
    while True:
        N = int(input())
        if 1 <= N:
            break
        else:
            print("invalid number")
            
    def test_prime(n):
        if n == 1:
            print("NO")
        elif n == 2:
            print("YES")
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    print("NO")
                    return
            print("YES")
    test_prime(N)