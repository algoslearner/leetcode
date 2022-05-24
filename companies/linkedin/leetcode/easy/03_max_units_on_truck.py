# https://leetcode.com/problems/maximum-units-on-a-truck/
'''
1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

 

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
 

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
'''

# boxCount =  min(maxUnitsBoxType[0], remainingTruckSize)
#################################################################################################################
# SORT
# TC: O(n log n)
# SC: O(1)

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:-x[1])
        maxunits = 0
        currSize = 0
        for numbox, unit in boxTypes:
            maxunits += unit * min(truckSize - currSize, numbox)
            currSize += min(truckSize - currSize, numbox)
        return maxunits
      
#################################################################################################################
# BUCKET SORT
# TC: O(n)
# SC: O(1)
# https://leetcode.com/problems/maximum-units-on-a-truck/discuss/1000343/countingbucket-sort-O(n)-faster-than-100

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # build up the bucket array, the indicies are the units per box
        # the value is the amount of boxes at that level
        boxes = [0] * 1001
        for bt in boxTypes:
            boxes[bt[1]] += bt[0]
        
        i, units = 1000, 0
        # start from the back since we want the most units per box
        while(truckSize and i > -1):
            if boxes[i] == 0:
                i-=1
                continue
            # take away as many boxes as we can at the 
            # level or the remaining boxes
            take_away = min(truckSize, boxes[i])
            
            units+= take_away*i
            boxes[i] -= take_away
            truckSize-= take_away
            i-=1
        
        return units
