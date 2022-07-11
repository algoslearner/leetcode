#
'''
Minimum Meeting Rooms (hard)#
Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

Example 1:

Meetings: [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
occur in any of the two rooms later.
Example 2:

Meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
Example 3:

Meetings: [[1,4], [2,3], [3,6]]
Output:2
Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
hold all the meetings.

Example 4:

Meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

Similar Problems#
Problem 1: Given a list of intervals, find the point where the maximum number of intervals overlap.

Problem 2: Given a list of intervals representing the arrival and departure times of trains to a train station, our goal is to find the minimum number of platforms required for the train station so that no train has to wait.

Both of these problems can be solved using the approach discussed above.

'''

##########################################################################################################################
# heap
# TC: O(n log n)
# SC: O(n)

def min_meeting_rooms(meetings):
  # sort the meetings by start time
  meetings.sort(key=lambda x: x.start)

  minRooms = 0
  minHeap = []
  for meeting in meetings:
    # remove all the meetings that have ended
    while(len(minHeap) > 0 and meeting.start >= minHeap[0].end):
      heappop(minHeap)
    # add the current meeting into min_heap
    heappush(minHeap, meeting)
    # all active meetings are in the min_heap, so we need rooms for all of them.
    minRooms = max(minRooms, len(minHeap))
  return minRooms



############################################################################################################################
'''
253. Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
'''
############################################################################################################################
# sorting
# TC: O(n log n)
# SC: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        numRooms = 0
        k = 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        
        for s in range(len(start)):
            if start[s] < end[k]: 
                numRooms += 1
            else: 
                k += 1
        return numRooms
