class Solution(object):
    def fizzBuzz(self, n):
        arr = []
        for i in range(0,n):
            i+=1
            val = str(i)
            
            if (i%3 == 0 and i%5 == 0):
                val = "FizzBuzz"
            elif i%3 == 0:
                val = "Fizz"
            elif i%5 == 0:
                val = "Buzz"
            
            arr.append(val)
        
        return arr
