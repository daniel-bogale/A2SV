# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def count_almost_primes(n):
    count = 0
    
    for x in range(2, n+1):
        divisors = 0
        num = x
        
        for i in range(2, num+1):
            if num % i == 0:
                is_prime = True
                for j in range(2, int(i**0.5)+1):
                    if i % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    divisors += 1
                    while num % i == 0:
                        num //= i
        if divisors == 2:
            count += 1
    
    return count

n = int(input())
print(count_almost_primes(n))

# MK