# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [0]*len(indices)
        for idx in indices:
            answer[indices[idx]] = s[idx]
        return ("").join(answer)
            
