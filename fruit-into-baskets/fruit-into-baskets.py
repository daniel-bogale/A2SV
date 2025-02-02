class Solution(object):
    def totalFruit(self, fruits):
        start=end=0
        max_len=0
        d={}
        while end < len(fruits):
            d[fruits[end]]=end
            if len(d)>2:
                min_val=min(d.values())
                start=min_val +1
                del d[fruits[min_val]]

            max_len=max(max_len,end-start+1)
            end+=1
        return max_len
