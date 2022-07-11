#
'''
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

Problem 1: Given a list of appointments, find all the conflicting appointments.

Example:
Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
Output: 
[4,5] and [3,6] conflict. 
[3,6] and [5,7] conflict.
'''

###################################################################################################################################
# sorting
# TC: O(N log N)
# SC: O(N)

def can_attend_all(intervals) -> bool:
  intervals.sort(key = lambda x : x[0])
  
  start, end = 0, 1
  for i in range(1, len(intervals)):
    if intervals[i][start] < intervals[i - 1][end]:
      return False
    
  return True

