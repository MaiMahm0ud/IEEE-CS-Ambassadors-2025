while True:
    S = input()
    if all(ch.isalpha() or ch ==',' for ch in S):
        break
    else:
        print("try again")
after_conv = ""
for ch in S:
    if ch.islower():
        after_conv += ch.upper()
    elif ch.isupper():
        after_conv += ch.lower()
    elif ch == ',':
        after_conv += ' '
print(after_conv)