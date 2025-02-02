class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return len(stack) == 0
