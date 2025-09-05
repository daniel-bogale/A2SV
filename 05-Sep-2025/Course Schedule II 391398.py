# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming_count = [0 for _ in range(numCourses)]

        queue = deque()
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming_count[course] += 1

        for course in range(numCourses):
            if incoming_count[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                incoming_count[neighbor] -= 1
                
                if incoming_count[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != numCourses:
            return []


        return order