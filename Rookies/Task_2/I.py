while True:
    S = input()
    if S.isalpha() and S.islower():
        break
    else:
        print("try again")
revS = ""
for i in S :
    revS = i + revS 
if(S == revS):
    print("YES")
else:
    print("NO")