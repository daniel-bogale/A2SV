# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        prev_even_sum=sum([num for num in nums if num%2==0 ])
        for query in queries:
            val,index=query
            new_val =nums[index] + val
            if new_val%2 ==0:
                if(nums[index] %2 == 0):
                    prev_even_sum+=val
                else:
                    prev_even_sum+= new_val
            else:
                if(nums[index]%2 == 0):
                    prev_even_sum-= nums[index]

            nums[index] += val
            ans.append(prev_even_sum)

        return ans
