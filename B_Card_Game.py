N = int(input())
nums = list(map(int,input().split()))
original_pos = {}
for i,num in enumerate(nums):
    original_pos[num] = original_pos.get(num,[])+[i]

nums.sort()

for i in range(N//2):
    left = original_pos[nums[i]]
    right = original_pos[nums[len(nums)-1]]
    print(left[0]+1, right[-1]+1)
    original_pos[nums[i]] = original_pos[nums[i]][1:] if len(original_pos[nums[i]]) > 0 else []
    original_pos[nums[len(nums)-1]] = original_pos[nums[len(nums)-1]][:-1] if len(original_pos[nums[len(nums)-1]]) > 0 else []
    nums = nums[:-1] if len(nums)>0 else []