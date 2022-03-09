'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''

# https://leetcode.com/problems/number-of-days-between-two-dates/discuss/551181/Python-cheat-function
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        return abs(int((datetime.datetime(y1,m1,d1)- datetime.datetime(y2,m2,d2)).days))

# Similar to https://leetcode.com/problems/day-of-the-year/discuss/355854/Python-Cheat
def ordinalOfDate(self, date):
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)

# Magical formula
# https://leetcode.com/problems/number-of-days-between-two-dates/discuss/517582/Python-Magical-Formula
'''
When m=1 or m=2 (January or February), we let m=13 or m=14 and let y decreased by 1. 
Imagine it is 13th or 14th month of the last year. 
By doing that, we let the magical formula also work for those two months. 
(153 * m + 8) // 5 is just a carefully designed way to record the days of each month. 

More specifically, it is designed to record the difference of days between two months. 
Suppose we have March 1st and April 1st, (153 * 3 + 8) // 5 = 93 while (153 * 4 + 8) // 5 = 124, 
the difference is 31 which is the number of days in March. 

Suppose we have April 1st to May 1st, (153 * 4 + 8) // 5 = 124 and (153 * 5 + 8) // 5 = 154, 
the difference is now 30 which is the number of days in April. You can also check other months.

I learned this formula somewhere else before. It is not something to come up with in minutes.
'''

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m < 3:
                m += 12
                y -= 1
            return 365 * y + y // 4 + y // 400 - y // 100 + d + (153 * m + 8) // 5
        
        return abs(f(date1) - f(date2))

