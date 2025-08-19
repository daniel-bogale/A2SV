# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dir = defaultdict(int)

        for num in nums:
            dir[num] += 1


        dir = dict(sorted(dir.items(), key=lambda item: item[1], reverse=True))
        ans = []
        for key , val in dir.items():
            if len(ans) == k:
                break
            ans.append(key)

        return ans        
