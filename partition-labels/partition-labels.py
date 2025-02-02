class Solution(object):
    def partitionLabels(self,s):
        last_right_index={c:i for i,c in enumerate(s)}
        cur=prev=0
        result=[]
        for i ,c in enumerate(s):
            cur=max(cur,last_right_index[c])
            if i==cur:
                result.append(cur-prev +1)
                prev=i+1
        return result
