while True:
    N =int(input())
    if 1 <= N <= 100:
       break
    else:
       print("Try again")
while True:
    A = list(map(int, input().split()))
    if len(A) != N:
        print(f"Please enter exactly {N} numbers")
        continue
    elif any(x < 1 or x > 100 for x in A):
        print("invalid input")
        continue
    else:
        break
def max_number(a_list):
    max_num = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > max_num:
            max_num = a_list[i]
    print(f"The maximum number : {max_num}")
    
def min_number(a_list):
    min_num = a_list[0] 
    for i in range(len(a_list)):
        if a_list[i] < min_num:
            min_num = a_list[i]
    print(f"The minimum number : {min_num}")    
    
def count_prime_num(a_list):
    count = 0
    for num in a_list:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    print(f"The number of prime numbers : {count}")
        
def palindrom_num(a_list):
    count = 0 
    for num in a_list:
        if str(num) == str(num)[::-1]:
            count += 1
    print(f"The number of palindrome numbers : {count}")
    
def num_with_max_divisors(a_list):
    max_divisors = 0
    result_number = 0

    for num in a_list:
        divisors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors += 1

        if divisors > max_divisors:
            max_divisors = divisors
            result_number = num
        elif divisors == max_divisors:
            result_number = max(result_number, num)

    print(f"The number that has the maximum number of divisors : {result_number}")
    
max_number(A)
min_number(A)
count_prime_num(A)
palindrom_num(A)
num_with_max_divisors(A)