class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        c_set=set()
        max_=0
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l+=1
            c_set.add(s[r])
            max_=max(max_,r-l+1)
        return max_
