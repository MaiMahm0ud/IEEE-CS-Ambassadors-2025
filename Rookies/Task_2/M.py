while True:
    S = input()
    if S.isalpha() and S.islower() and 5 <= len(S) <= 10000:
        break
    else:
        print("try again")
word = "hello"
x = 0
for ch in S:
    if ch == word[x]:
        x += 1
        if x == len(word):
            break
if x == len(word):
    print("YES")
else:
    print("NO")