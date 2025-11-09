# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

from collections import defaultdict
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dir , ans = defaultdict() , [None] * len(score)
        for i in range(len(score)):
            dir[score[i]] = i

        score.sort(reverse = True)    

        for i in range(len(score)):
            if i == 0 :
                ans[dir[score[i]]] = 'Gold Medal'
            elif i == 1:    
                ans[dir[score[i]]] = 'Silver Medal'
            elif i == 2:    
                ans[dir[score[i]]] = 'Bronze Medal'
            else:
                ans[dir[score[i]]] = str(i+1)    

        return ans        
#AM