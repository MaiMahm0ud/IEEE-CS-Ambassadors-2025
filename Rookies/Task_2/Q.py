while True:
    S = input().split()
    if all(ch.isalpha() or ch == ' ' for ch in S) and S != "":
        break
    else:
        print("try again")
rev_S = []
for word in S:
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    rev_S.append(reversed_word)
        
final_S = ' '.join(rev_S)
print(final_S)