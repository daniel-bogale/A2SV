class Solution:
    def isValid(self, s):
        stack=[]
        closing={")":"(","]":"[","}":"{"}
        for i in s:
            if i in closing.values():
                stack.append(i)
            elif stack and closing[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[]
