class Solution:
    def topKFrequent(self, nums, k):
        count=Counter(nums)
        output=[]
        inverse = [(value, key) for key, value in count.items()]
        inverse.sort(reverse=True)
        for i in range(0,k):
            a=inverse[i][1]
            output.append(a)
        return output
