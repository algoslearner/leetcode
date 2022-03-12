'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        k = None
        prev = curr = 0
        
        for num in sorted(count):
            earn = num * count[num]
            
            if num - 1 == k:
                prev, curr = curr, max(prev + earn, curr)
            else:
                prev, curr = curr, curr + earn
                
            k = num
        
        return curr
Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
'''

##############################################################################################################
# A slight modification of House Robber problem .
'''
Reduce it to the house rober problem by grouping repeated numbers together and sorting the unique numbers.
If the current number - 1 is equal to the previous number, then we have to make a rob-or-not-rob decision, else we can just take the number.
'''

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        k = None
        prev = curr = 0
        
        for num in sorted(count):
            earn = num * count[num]
            
            if num - 1 == k:
                prev, curr = curr, max(prev + earn, curr)
            else:
                prev, curr = curr, curr + earn
                
            k = num
        
        return curr
