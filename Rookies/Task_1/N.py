A, B = map(int, input().split())
S = input().strip()
 
valid = True
 
 
if len(S) != A + B + 1:
    valid = False
else:
    if S[A] != '-':
        valid = False
    else:
        for i in range(len(S)):
            if i != A:
                if not S[i].isdigit():
                    valid = False
                    break
 
print("Yes" if valid else "No")