class Solution:
    def longestSubarray(self, nums, limit):
        
        min_dq = deque()
        max_dq = deque()

        start = 0
        max_len = 0

        for i in range(len(nums)):

            while min_dq and abs(nums[i] - min_dq[0][0]) > limit:
                start = min_dq.popleft()[1] + 1

            while max_dq and abs(nums[i] - max_dq[0][0]) > limit:
                
                start = max(start, max_dq.popleft()[1] + 1)

            while min_dq and min_dq[-1][0] >= nums[i]:
                
                min_dq.pop()
            min_dq.append([nums[i], i])

            while max_dq and max_dq[-1][0] <= nums[i]:
                max_dq.pop()
            max_dq.append([nums[i], i])

            max_len = max(max_len, (i - start) + 1)

        return max_len
            
