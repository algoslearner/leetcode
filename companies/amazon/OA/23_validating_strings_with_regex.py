# https://leetcode.com/discuss/interview-question/1473342/Amazon-OA
# refer for screenshots of question

'''
Given a list of strings made up of characters 'a' and 'b', create a regular expression that will match strings that begin and end with same letter.
'''

####################################
# SOLUTION 1

Simple and Intuitive answer which passed all test cases for me: ( a | b | (a.*a) | (b.*b) )
Notes:

.* can match anything, including empty string.
| stands for OR

####################################
# SOLUTION 2

it should be r'^(.).*\1$|[ab]$'

####################################
# SOLUTION 3

This should be the NG-OA demo/practice question, I got this 30/09/2021,
The solution should be: r'^[a-z]$|^([a-z]).*\1$'
  
  I guess I found the solution. reg = r"^([ab])(?:.*?\1)?$"
