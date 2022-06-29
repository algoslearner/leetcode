# https://leetcode.com/problems/course-schedule-iii/
'''
630. Course Schedule III

There are n different online courses numbered from 1 to n. 
You are given an array courses where courses[i] = [durationi, lastDayi] 
indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

 

Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0
 

Constraints:

1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104
'''

##########################################################################################################
# https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation
# maxheap
# TC: O(N log k)
# SC: O(k)

'''
Sort all the courses by their ending time. When considering the first K courses, they all end before end. A necessary and sufficient condition for our schedule to be valid, is that (for all K), the courses we choose to take within the first K of them, have total duration less than end.

For each K, we will greedily remove the largest-length course until the total duration start is <= end. To select these largest-length courses, we will use a max heap. start will maintain the loop invariant that it is the sum of the lengths of the courses we have currently taken.

Clearly, this greedy choice makes the number of courses used maximal for each K. When considering potential future K, there's never a case where we preferred having a longer course to a shorter one, so indeed our greedy choice dominates all other candidates.
'''

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        maxheap = []
        start = 0
        for i in sorted(courses, key = lambda x: x[1]):
            start += i[0]
            heapq.heappush(maxheap, -i[0])
            while start > i[1]:
                start += heapq.heappop(maxheap)
        return len(maxheap)

