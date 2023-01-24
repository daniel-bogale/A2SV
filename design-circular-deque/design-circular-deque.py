class MyCircularDeque:

    def __init__(self, k):
        self.max_size =k
        self.cq = [None]*self.max_size
        self.head =0
        self.tail =0
        self.count = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        else:
            self.head = (self.head -1)%self.max_size
            self.cq[self.head] = value
            self.count += 1
            return True
        

    def insertLast(self, value):
        if self.isFull():
            return False
        else:
            self.cq[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.count += 1
            return True
        
        

    def deleteFront(self):
          if self.isEmpty():
            return False
          else:
            self.count -= 1
            self.head = (self.head + 1) % self.max_size
            return True
        

    def deleteLast(self):
        if self.isEmpty():
            return False
        else:
            self.tail = (self.tail - 1) % self.max_size
            self.count -= 1
            return True
        

    def getFront(self):
         if self.isEmpty():
            return -1
         else:
            return self.cq[self.head]
        

    def getRear(self):
         if self.isEmpty():
            return -1
         else:
            return self.cq[self.tail - 1]
        

    def isEmpty(self):
        return self.count == 0
        

    def isFull(self):
        return self.count == self.max_size
        
