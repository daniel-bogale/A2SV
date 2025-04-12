import sys
MOD = 10**9 + 7
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    
    max_ending_here = 0
    max_so_far = 0
    for num in a:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    if max_so_far <= 0:
        # Best is to add 0 k times
        res = total_sum % MOD
    else:
        # Compute (2^k - 1) mod MOD
        power = pow(2, k, MOD)
        term = (power - 1) % MOD
        term = (term * max_so_far) % MOD
        res = (total_sum + term) % MOD
    
    print(res)
