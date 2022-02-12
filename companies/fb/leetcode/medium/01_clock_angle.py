'''
1344. Angle Between Hands of a Clock

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

Example 1:
Input: hour = 12, minutes = 30
Output: 165

Example 2:
Input: hour = 3, minutes = 30
Output: 75

Example 3:
Input: hour = 3, minutes = 15
Output: 7.5
'''

# math
# TC : O(1)
# SC : O(1)

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        minute_angle = minutes * one_min_angle
        hour_angle = (hour % 12 ) * one_hour_angle
        hour_angle +=  minutes/60.0 * one_hour_angle
        
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360-diff)
