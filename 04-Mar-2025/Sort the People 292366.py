# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            max_idx = i
            for j in range(i, len(heights)):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            heights[i],heights[max_idx] = heights[max_idx],heights[i]
            names[i],names[max_idx] = names[max_idx],names[i]
        print(heights)
        return names
