"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""
import collections
def courseSchedule(numCourses, prereq):

    graph = collections.defaultdict(list)
    visited = set()

    for u, v in prereq:
        graph[u].append(v)

    def dfs(index):
        if index in visited:
            return False
        
        dependent = graph[index]

        if dependent == []:
            return True
        
        visited.add(index)
        
        
        for course in dependent:
            if not dfs(course):
                return False
            
        visited.remove(index)
        graph[index] = []
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True


numCourses = 2
prerequisites = [[1,0]]
print(courseSchedule(numCourses,prerequisites))

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(courseSchedule(numCourses,prerequisites))


numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(courseSchedule(numCourses,prerequisites))