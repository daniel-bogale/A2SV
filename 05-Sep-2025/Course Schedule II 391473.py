# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)] 
        
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        for node in range(numCourses):
            if colors[node] == 0:
                if not self.topSort(node, colors, graph, order):
                    return []  # cycle detected
        
        return list(reversed(order))
    
    def topSort(self, node, colors, graph, order):
        if colors[node] == 1:
            return False
        if colors[node] == 2:  
            return True
        
        colors[node] = 1  

        for nei in graph[node]:
            if not self.topSort(nei, colors, graph, order):
                return False
        
        colors[node] = 2 
        order.append(node)
        return True
