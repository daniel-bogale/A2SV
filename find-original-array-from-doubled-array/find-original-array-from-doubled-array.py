class Solution(object):
    def findOriginalArray(self,changed):
        count=Counter(changed)
        result=[]
        changed.sort()
        for num in changed:
            if count[num]==0:continue
            if count[2*num]==0: return []
            if num==0 and count[num]<=1:return []
            result.append(num)
            count[num]-=1
            count[2*num]-=1
        return result
