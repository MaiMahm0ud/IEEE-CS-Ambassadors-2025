while True:
    Q = int(input())
    if 1 <= Q <= 2:
        break
    else:
        print("Try again")

Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
if Q == 1:
    S = input()
    result =""
    for ch in S:
        if ch in Original:
            index = Original.index(ch)
            result += Key[index]
        else:
            result += ch
    print(result)
elif Q == 2:
    S = input()
    result =""
    for ch in S:
        if ch in Key:
            index = Key.index(ch)
            result += Original[index]
        else:
            result += ch
    print(result)