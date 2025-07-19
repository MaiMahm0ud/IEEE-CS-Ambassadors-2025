while True:
    T = int(input())
    if 1 <= T <= 100:
        break
    else:
        print("Test cases must be between 1 ,100")
for _ in range(T):
    while True:
        S = input()
        if S.isalpha() and S.islower():
            break
        else:
            print("try again")
    if len(S) <= 10:
        print(S)
    else:
        length = len(S)-2
        print(S[0] + str(length) + S[len(S)-1])
