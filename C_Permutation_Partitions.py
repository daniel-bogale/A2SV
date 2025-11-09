MOD = 998244353

n, k = map(int, input().split())
p = list(map(int, input().split()))

# Find positions of the k largest elements
threshold = n - k + 1
positions = [i for i, val in enumerate(p) if val >= threshold]

# Sum of k largest numbers
max_sum = k * (2 * n - k + 1) // 2

# Product of distances between consecutive positions
ways = 1
for i in range(1, len(positions)):
    ways = (ways * (positions[i] - positions[i - 1])) % MOD

print(max_sum, ways)
