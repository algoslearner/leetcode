'''
Write a function that when given a time, returns the smallest angle between the minute and hour hands on an analog clock.
Signature
double getSmallestClockAngle(String timeString, String unit)
Input
timeString: a representation of  the time in a string with format hh:mm
unit: string which determines if the return value is in degrees or radians
Output
an integer for degrees and accurate to 4 decimal places for radians.
Note: use π (pi) functions provided by the language of choice.
Example 1:
Input:     
timeString = '03:00’ 
unit = ‘radians’
Output:  1.5708
Example 2:
Input:     
timeString  = ‘09:30’
unit = ‘degrees’
Output:  105
Reference hints:
There are 360 degrees in a circle.
There are 2π radians in a circle
An analog clock is divided in to 12 sectors, each sector represents 30 degrees (360/12 = 30)
'''

# TC : O(1)
# SC : O(1)
# math

import math

def getSmallestClockAngle(timeString, unit):
  # extract time from string
  time = timeString.split(":")
  hour = int(time[0])
  minute = int(time[1])
  
  one_minute_angle = 6
  one_hour_angle = 30
  if unit == "radians":
    one_minute_angle = (2 * math.pi) / 60
    one_hour_angle = (2 * math.pi) / 12
  
  minute_angle = minute * one_minute_angle
  hour_angle = (hour % 12 + minute/60.0 ) * one_hour_angle 
  diff = abs(hour_angle-minute_angle)
  
  if unit == "radians":
    diff = round(diff,4)
  
  return min(diff, 360-diff)
