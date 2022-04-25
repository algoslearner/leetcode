# https://leetcode.com/discuss/interview-question/862371/VISA-online-Assignment/708848
'''
A video game developer is developing a game in which the character makes their way through several segments of a level. In each segment, if the character collects a coin the player scores 1 point. However, if the segment does not have a coin 1 point is deducted from the total score.Player 1 always begins the level and, at some point, the game play is turned over to Player 2 to complete the level. Player1's goal is to achieve heigher score than Player 2 once the level is completed. Given the segment status(whether they contain the coin or not), find the minimum number of segments Player1 should play so that, in the end Player1's score is greater than Player2.

Example: [1,1,0,1]
Player 1 has the follwoing option:

Play 0 segment- Player1's score 0 and Player2's score ->3-1=2(3 points for segments with coin and -1 for no coin segment)
Play 1 segment- Player1's score 1 and Player2's score -> 2-1=1
Play 2 segment- Player1's score 2 and Player2's score -> 1-1=0
So the answer is 2.

What can be optimized solution
'''

#####################################################################################
'''
#Brute force approach to calculate total score and navigate again to check player scores. It worked and all TC passed.
O(n) solution

Run a loop, sum up the total score
Run another loop keep adding up p1's score
Total - p1 becomes p2's score
When p1 > p2 break and return the result
'''

def game(nums):
  s = sum(nums)
  cur_sum = 0
  for i in range(len(nums)):
    cur_sum += nums[i]
    if cur_sum > s-cur_sum:
      return i+1
  return -1
