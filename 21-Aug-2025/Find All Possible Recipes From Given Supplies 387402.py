# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        ans = []
        seen = set(supplies)
        dq = deque([(r, ing) for r, ing in zip(recipes, ingredients)])
        

        prev_size = len(seen) - 1 
        
        while len(seen) > prev_size:
            prev_size = len(seen)
            for _ in range(len(dq)):
                r, ing = dq.popleft()
                if all(i in seen for i in ing):
                    ans.append(r)
                    seen.add(r)
                else:
                    dq.append((r, ing))
        return ans
        