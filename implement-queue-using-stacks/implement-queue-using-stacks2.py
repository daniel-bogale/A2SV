class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        return self.stack1.append(x)

    def update(self):
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())

    def pop(self):
        if len(self.stack2)==0:
            self.update()
        return self.stack2.pop()
        
    def peek(self):
        if not self.empty():
            if len(self.stack2)==0:
                self.update()
            return self.stack2[-1]
    def empty(self):

        return len(self.stack2) == 0 and len(self.stack1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
