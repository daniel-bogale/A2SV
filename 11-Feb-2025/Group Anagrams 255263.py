# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = ["".join(sorted(s)) for s in strs]
        groups = {

        }
        for i,value in enumerate(sorted_strings):
            groups[value] = groups.get(value, [])  + [strs[i]]

        answer = []
        for g_id in groups:
            answer.append(groups[g_id])

        return answer