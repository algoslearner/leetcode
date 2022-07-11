#
'''
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. 
Our goal is to find out if there is a free interval that is common to all employees. 
You can assume that each list of employee working hours is sorted on the start time.

Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employees are free between [3,5].
Example 2:

Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employees are free between [4,6] and [8,9].
Example 3:

Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employees are free between [5,7].
'''

#########################################################################################################################################
# min heap
# TC: O(n log k)
# SC: O(k)

def find_employee_free_time(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        # if previousInterval is not overlapping with the next interval, insert a free interval
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            previousInterval = queueTop.interval
        else:  # overlapping intervals, update the previousInterval if needed
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))

    return result


#############################################################################################################################
# sorting
# TC: O(n log n)
# SC: O(n)
# https://leetcode.com/problems/employee-free-time/discuss/170551/Simple-Python-9-liner-beats-97-(with-explanation)
'''
Key points:

1. recognize that this is very similar to merging intervals (https://leetcode.com/problems/merge-intervals/description/)
2. it doesn't matter which employee an interval belongs to, so just flatten
3. can build result array while merging, don't have to do afterward (and don't need full merged arr)
'''

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, end = [], ints[0].end
        for i in ints[1:]:
            if i.start > end:
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res
