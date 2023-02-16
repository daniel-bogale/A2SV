class Solution(object):
    def sortSentence(self, s):
        strArr = s.split()
        length =len(strArr)
        sorted = [""]*length
        for word in strArr:
            sorted[int(word[-1])-1] = word[0:-1]
        
        return (" ").join(sorted)
    
   
