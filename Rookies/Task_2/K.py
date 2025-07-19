while True:
    N = int(input())
    if N < 1 or N > 50 :
        print("N must be between 1 , 50")
        continue
    else:
        break
for _ in range(N):
    while True:
        user_input = input().strip().split()
        if len(user_input) != 2:
            print("Please enter exactly two words separated")
            continue
        S , T = user_input
        if not (S.isalpha() and T.isalpha()):
            print("Only letters are allowed")
            continue
        if len(S) < 1:
            print("The first word must be at least 1 character")
            continue
        if len(T) > 50:
            print("The second word must be 50 characters or fewer")
            continue
        break
    new_str = ""
    max_length = max(len(S), len(T))
    for i in range(max_length):
        if i < len(S):
            new_str += S[i]
        if i < len(T):
            new_str += T[i]

    print(new_str)