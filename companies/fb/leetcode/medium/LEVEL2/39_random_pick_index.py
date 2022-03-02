'''
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
 

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
target is an integer from nums.
At most 104 calls will be made to pick.
'''

# RESeRVOIra SAMPLING
# Time : O(N)
# Space: O(1)
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, target: int) -> int:
        count = idx = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            if count == 0:
                idx = i
                count = 1
            else:
            # this random will already give me numbers
            # between 0 and cnt inclusive
            # so for 2nd number I am getting random number 0 and 1
            # so each having a probability of 1/2
            # similarly for three numbers it will be 1/3
                rnd = random.randint(0, count)
                if (rnd == count):
                    idx = i
                count += 1
    
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
