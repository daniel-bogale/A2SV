n = int(input())
arr = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes_upto(n):
    return [x for x in range(2, n + 1) if is_prime(x)]

all_primes = get_primes_upto(arr[-1])

num_primes = [set() for _ in arr]


for i,num in enumerate(arr):
    for prime in all_primes:
        if num % prime ==0:
            num_primes[i].add(prime)
            
sequence_count = [0 for _ in all_primes]

prev = num_primes[0]
count = 0

for i in range(1,len(num_primes)):
    primes = num_primes[i]
    co_prime = True
    for prime in primes:
        if prime in prev:
            co_prime=False
            break
    if not co_prime:
        count +=1
    prev = primes
        
print(count)