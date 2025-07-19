N, Q = map(int, input().split())
while True:
    s = input().strip()
    if N == len(s) and s.islower() and s.isalpha():
        break
    else:
        print("try again")

for _ in range(Q):
    query = input().split()
    cmd = query[0]
    
    if cmd == "pop_back":
        s = s[:-1]
    elif cmd == "front":
        print(s[0])
    elif cmd == "back":
        print(s[-1])
    elif cmd == "sort":
        l, r = int(query[1]), int(query[2])

        l_idx = l - 1
        r_idx = r

        sorted_part = ''.join(sorted(s[l_idx:r_idx]))
        s = s[:l_idx] + sorted_part + s[r_idx:]
    elif cmd == "reverse":
        l, r = int(query[1]), int(query[2])
        l_idx = l - 1
        r_idx = r

        reversed_part = s[l_idx:r_idx][::-1]
        s = s[:l_idx] + reversed_part + s[r_idx:]
    elif cmd == "print":
        pos = int(query[1])
        print(s[pos-1])
    elif cmd == "substr":
        l, r = int(query[1]), int(query[2])
        l_idx = l - 1
        r_idx = r
        print(s[l_idx:r_idx])
    elif cmd == "push_back":
        x = query[1]
        s += x