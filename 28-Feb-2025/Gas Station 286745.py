# Problem: Gas Station - https://leetcode.com/problems/gas-station/

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        
        start, curr_gas = 0, 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            curr_gas += diff
            
            if curr_gas < 0:
                start = i + 1
                curr_gas = 0

        return start