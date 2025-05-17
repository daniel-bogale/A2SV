import math
import sys

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        total_sum = n * (n + 1) // 2
        if is_perfect_square(total_sum):
            print(-1)
        else:
            permutation = []
            left = 1
            right = n
            toggle = True  # True for right, False for left
            while left <= right:
                if toggle:
                    permutation.append(right)
                    right -= 1
                else:
                    permutation.append(left)
                    left += 1
                toggle = not toggle
            # Verify the permutation (optional for debugging)
            # prefix_sum = 0
            # valid = True
            # for num in permutation:
            #     prefix_sum += num
            #     if is_perfect_square(prefix_sum):
            #         valid = False
            #         break
            # if not valid:
            #     print("Invalid permutation found for n =", n)
            #     continue
            print(' '.join(map(str, permutation)))

solve()