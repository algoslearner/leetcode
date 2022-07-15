# https://leetcode.com/problems/count-integers-with-even-digit-sum/
'''
2180. Count Integers With Even Digit Sum

Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

 

Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
 

Constraints:

1 <= num <= 1000
'''

#######################################################################################################################
# TC: O(n)
# SC: O(1)

class Solution:
    def digitsum(self, n: int) -> int:
        digits_sum = 0
        while n > 0:
            digit = n % 10
            digits_sum += digit
            n = n // 10
        return digits_sum
        
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(1, num+1):
            if self.digitsum(n) % 2 == 0:
                count += 1
        return count
       
#######################################################################################################################
# tc: O(log n)
# sc: O(1)
# So the evens can be given as num//2 in all the cases except when the number itself is even but digit sum is odd. Example:10, 12, 30 In such cases the even numbers would less by 1 as that particular number is not a valid number.

 def countEven(self, num: int) -> int:
        n, dSum = num, 0
        while n > 0: # Calculate digit sum of numbers
            dSum += n%10
            n = n//10
        if num % 2 == 0 and dSum % 2 == 1:
            return num//2 - 1
        return num//2
