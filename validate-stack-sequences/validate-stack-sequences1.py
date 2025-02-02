
class Solution:
    def validateStackSequences(self, pushed, popped):
        n = len(pushed)
        i=j=top=0
        while i < n:
            if top >= 0 and popped[j] == pushed[top]:
                j += 1
                top -= 1
            else:
                top += 1
                i += 1
                if i < n:
                    pushed[top] = pushed[i]
        return top == 0
