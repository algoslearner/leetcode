#
'''
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. 
All other (not-happy) numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3 ^2
2 
2
 +3 
2
 
 = 4 + 9 = 13
1^2 + 3^2
1 
2
 +3 
2
 
 = 1 + 9 = 10
1^2 + 0^2
1 
2
 +0 
2
 
 = 1 + 0 = 1
Example 2:

Input: 12   
Output: false (12 is not a happy number)  
Explanations: Here are the steps to find out that 12 is not a happy number:
1^2 + 2 ^2
1 
2
 +2 
2
 
 = 1 + 4 = 5
5^2
5 
2
 
 = 25
2^2 + 5^2
2 
2
 +5 
2
 
 = 4 + 25 = 29
2^2 + 9^2
2 
2
 +9 
2
 
 = 4 + 81 = 85
8^2 + 5^2
8 
2
 +5 
2
 
 = 64 + 25 = 89
8^2 + 9^2
8 
2
 +9 
2
 
 = 64 + 81 = 145
1^2 + 4^2 + 5^2
1 
2
 +4 
2
 +5 
2
 
 = 1 + 16 + 25 = 42
4^2 + 2^2
4 
2
 +2 
2
 
 = 16 + 4 = 20
2^2 + 0^2
2 
2
 +0 
2
 
 = 4 + 0 = 4
4^2
4 
2
 
 = 16
1^2 + 6^2
1 
2
 +6 
2
 
 = 1 + 36 = 37
3^2 + 7^2
3 
2
 +7 
2
 
 = 9 + 49 = 58
5^2 + 8^2
5 
2
 +8 
2
 
 = 25 + 64 = 89
Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.
'''

##################################################################################################################################################
# TC: O(log n)
# SC: O(1)

def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()

