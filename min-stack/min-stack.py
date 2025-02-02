class MinStack:
    def __init__(self):
        self.stack = []
        self.minimums = deque()

    def push(self, val):
        self.stack.append(val)
        if not self.minimums:
            self.minimums.append(val)
            return
            
        if val <= self.minimums[0]:
                self.minimums.appendleft(val)
                return
        

    def pop(self):
        val = self.stack.pop()
        if self.minimums[0] == val:
            self.minimums.popleft()
            return
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.minimums[0], self.minimums[-1])
