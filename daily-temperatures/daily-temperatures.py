class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0]*len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1] ]< v:
                indexold = stack.pop()
                ans[indexold] = i - indexold
            stack.append(i)
        return ans
        #hash wont work because  tempa can duplicate, store the indexes in the stack 
