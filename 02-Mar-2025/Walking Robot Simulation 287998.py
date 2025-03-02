# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        obstacles = {tuple(x) for x in obstacles}

        current_dir_idx = 0
        current_pos = (0,0)
        max_distance = 0
        for command in commands:
            if command == -1:
                current_dir_idx = (current_dir_idx + 1)%4
            elif command == -2:
                current_dir_idx = (current_dir_idx + 3)%4
            else:
                current_dir = directions[current_dir_idx]
                current_x_dir = current_dir[0]
                current_y_dir = current_dir[1]
                for i in range(command):
                    next_pos = (current_pos[0] + (1*current_x_dir),current_pos[1]+(1*current_y_dir))
                    if next_pos in obstacles:
                        break
                    else:
                        current_pos = next_pos
                        max_distance = max(max_distance, next_pos[0]**2+next_pos[1]**2)
        return max_distance
