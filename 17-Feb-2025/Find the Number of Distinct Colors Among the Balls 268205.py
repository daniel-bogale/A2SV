# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_count = {}
        idx_color = {}
        result = []
        for idx, new_color in queries:
            old_color = idx_color.get(idx, 0)
            # Set color to idx->color dict
            idx_color[idx] = new_color

            color_count[new_color] = color_count.get(new_color, 0) + 1

            if old_color != 0 and old_color in color_count:
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    color_count.pop(old_color)
            
            result.append(len(color_count.keys()))

        return result