class Solution(object):
    def subarraySum(self, nums, k):
        result=0
        current_sum=0
        prefix_sum={0:1}
        for n in nums:
            current_sum+=n
            diff=current_sum-k
            result+=prefix_sum.get(diff,0)
            prefix_sum[current_sum]=1+prefix_sum.get(current_sum,0)
        return result
