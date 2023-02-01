
class Solution(object):
    def compress(self,chars):
        final_index=0
        i=0
        while i< len(chars):
            letter=chars[i]
            count=0
            while i< len(chars) and chars[i]==letter:
                count+=1
                i+=1
            chars[final_index]=letter 
            final_index+=1
            if count>1:
                for c in str(count):
                    chars[final_index]=c
                    final_index+=1
        return final_index
