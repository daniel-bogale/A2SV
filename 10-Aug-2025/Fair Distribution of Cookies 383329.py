# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if n == k:
            return max(cookies)
        
        min_unfairness = float("inf")
        distribution = [0]* k


        def backtracking(i):
            nonlocal min_unfairness
            if i == n:
                min_unfairness = min(min_unfairness, max(distribution))
                return
            elif max(distribution)>min_unfairness:
                return
            else:
                for kid_idx in range(k):
                    distribution[kid_idx] += cookies[i]
                    backtracking(i+1)
                    distribution[kid_idx] -= cookies[i]
        
        backtracking(0)
        return min_unfairness