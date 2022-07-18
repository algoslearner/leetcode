'''
1136. Parallel Courses : https://leetcode.com/problems/parallel-courses/

You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.

 

Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
 

Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
'''

###################################################################################################################
# TOPOLOGICAL SORTING
# TC: O(E)
# SC: O(N)

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        semesters = 0
        sortedOrder = []
        
        # initializing graph
        indegree = {i: 0 for i in range(1, N+1)}
        adj_list_graph = {i: [] for i in range(1, N+1)}
        
        # build graph
        for prereq in relations:
            parent, child = prereq[0], prereq[1]
            adj_list_graph[parent].append(child)
            indegree[child] += 1
        
        # find all sources
        sources = deque()
        for key in indegree:
            if indegree[key] == 0:
                sources.append(key)
        
        # count number of semesters for each set of source-courses
        while sources:
            semesters += 1
            course_count = len(sources)
            while course_count > 0:
                curr = sources.popleft()
                sortedOrder.append(curr)
                course_count -= 1
                for child in adj_list_graph[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0: sources.append(child)
        
        # check if all courses are taken
        if len(sortedOrder) == N:
            return semesters
        else:
            return -1
        
