# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = j = matches = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
            j += 1
        return matches
