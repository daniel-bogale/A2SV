# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         friends = [i+1 for i in range(n)]
#         i = 0
#         while len(friends) > 1:
#             current_len = len(friends)
#             print(friends,current_len, "friends","len")
#             i += k-1
#             idx = i% current_len
#             print(idx,i,"idx")
#             friends.pop(idx)

#         print(friends, len(friends), "friends","len", "___=====")

        
#         return friends[0]
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i + 1 for i in range(n)]
        i = 0  
        while len(friends) > 1:
            current_len = len(friends)
            i = (i + k - 1) % current_len  
            friends.pop(i)  
        
        return friends[0]
 