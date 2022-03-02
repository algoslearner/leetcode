'''
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

# https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation
# Very similar with what we do in real life. Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).
 
 def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms
      
      
########################## SHORT VERSION ####
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
