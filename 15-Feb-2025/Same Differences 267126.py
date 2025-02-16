# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import Counter
N = int(input())
for i in range(N):
    length= int(input())
    nums = list(map(int,input().split()))
    count = 0
    for i,num in enumerate(nums):
        nums[i] = num - i
        
    frequency = Counter(nums)
    for key, value in frequency.items():
        if value >=2:
            count += int((value*(value-1))/2)
    print(count)