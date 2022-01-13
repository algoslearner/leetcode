'''
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
'''

# Time complexity: O(log(n))
# Space complexity: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return math.sqrt(num)
        
        left = 0
        right = num
        while left <= right:
            mid = left +(right - left)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid - 1
            else:
                left = mid+1
        return False
