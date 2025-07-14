N = int(input())
A = list(map(int, input().split()))
sum = 0
for n in A:
    num = int(n)
    sum = sum + num
    
if sum < 0 :
    sum = -sum
    
print(sum)