import re
while True:
    S = input().strip()

    if all(ch.isalpha() or ch in " ,.!?" or ch.isspace() for ch in S):
        break
    else:
        print("Invalid input")

words = re.split(r'[ ,.!?]+', S)
words = [word for word in words if word]
print(len(words))