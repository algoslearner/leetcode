# https://leetcode.com/discuss/interview-question/1952215/Amazon-or-OA
# https://leetcode.com/discuss/interview-question/1761729/Amazon-New-Grad-or-OA-or-Pascal-Triangle-Decryption

###################################################################################################################
# https://www.chegg.com/homework-help/questions-and-answers/order-ensure-maximum-security-developers-xyz-employ-multiple-encryption-methods-keep-user--q95120166
###################################################################################################################

'''
In order to ensure maximum security, the developers at xyz employ multiple encryption methods to keep user data protected.
In one method, numbers are encrypted using a scheme called 'Pascal Triangle". When an array of digits is fed to this system, it sums the adjacent digits. It then takes the rightmost digit (least significant digit) of each luge is repeated addition for the next step. Thus, the number of digits in each step is reduced by 1. This procedige until there are only 2 digits left, and this sequence of 2 digits forms the encrypted number.
Given the initial sequence of the digits of numbers, find the encrypted number. You should report a string of digits representing the encrypted number.
Function Description
Complete the function getEncryptedNumber in the editor below.
getEncryptedNumber has the following parameter:
int numbers[n]: the initial sequence of digits
Returns
string: the encrypted number represented as a string of 2 characters.
Constraints
2 <= numbers.length <= 5.10^3
0 <= numbers[1] ≤ 9
Sample Input For Custom Testing
numbers = [1, 2, 3, 4], n = 4
Sample Output
82
Explanation
The encryption occurs as follows: [1, 2, 3, 4] -> [3, 5, 7] -> [8, 2].
Another Input
numbers = [4, 5, 6, 7], n = 4
Sample Output
04
Explanation
The encryption occurs as follows: [4, 5, 6, 7] -> [9, 1, 3] -> [0, 4].
'''

'''
# https://leetcode.com/discuss/interview-question/1761729/Amazon-New-Grad-or-OA-or-Pascal-Triangle-Decryption
Given an array of integers, we sum neighbouring elements like pascal's triangle until only two integers remain and take those to be the output. 
During the process, if the sum of two elements is greater than or equal to 10, 
we only take the digit place to the next level. Sorry if the description isn't clear enough, I included a picture to demonstrate the idea.
'''

###################################################################################################################
# SOLUTION: 
# run a while loop with condition that the list is greater than 2 elements. 
# At each step, traverse through the list adding adjacent numbers together and replacing the left one with the sum. 
# Then once you finish, delete the last element in the list.

# TC: O(N^2)

def invertedTriangle(self,arr):
        len_ = len(arr)
        if len_ < 3:
            return arr
        cnt = 1
        while arr:
            if cnt == len_:
                len_-= 1
                cnt = 1
                arr.pop(0)
            if len_ == 2:
                return arr
            sum_ = (arr.pop(0) + arr[0])%10
            arr.append(sum_)
            cnt+=1
            
###################################################################################################################
# https://www.chegg.com/homework-help/questions-and-answers/taking-change-temperature-data-n-days-aggregate-temperature-change-evaluated-ith-day-maxim-q92661318
# Please look at this link for question screenshots
###################################################################################################################

'''
Taking the change in temperature data of n days, 
the aggregate temperature change evaluated on the ith day 
is the maximum of the sum of the changes in temperatures until the ith day, 
and the sum of the change in temperatures in the next (n. i) days, with the ith day temperature change included in both. 

Given the temperature data of n days, find the maximum aggregate temperature change evaluated among all the days. 

Example tempChange = [6, -2,5) 
The aggregate temperature change on each day is evaluated as: 
Day 1 
Day 2 Tampere Charger Temperature Change Tere Change Age Temperature Tempere Changes Акуприн тинтуннилин сыни он так, + 4 
Day 3 . Temer Change
For day 1, there are no preceding days' information, but the day itself is included in the calculation. Temperature changes = [6] for the before period. 
For succeeding days, there are values (6,-2,5) and 6 +(-2) + 5 = 9. Again, the change for day 1 is included. The maximum of 6 and 9 is 9. For day 2, consider [6, -2] -> 6+(-2) = 4, and [-2,5) - >(-2) + 5 = 3. The maximum of 3 and 4 is 4. For day 3, consider [6, -2, 5] -> 6+(-2) + 5 = 9, and [5). The maximum of 9 and 5 is 9. The maximum aggregate temperature change is max(9,4, 9) = 9. Function Description Complete the function getMaxAggregate TemperatureChange in the editor below. getMaxAggregate TemperatureChange has the following parameter: int tempChange[n]: the temperature change data of n days Returns long: the maximum aggregate temperature change
Constraints • 1sns 105 • -10° s tempChange[i]109 where, 1 sis n.
Sample Input For Custom Testing STDIN FUNCTION I 3 a tempChange() size n = 3 tempChange = (-1, 2, 3] a WN -1 2 3 Sample Output 5 Temperature changes before and after each day: Day 1: (-1), (-1, 2, 3] -> max(-1, 4) = 4 Day 2: (-1,2], [2, 3] -> max(1,5) = 5 Day 3: (-1,2, 3], [3] -> max(4, 3) = 4 Sum each array and take their maximum. The second day is optimal with aggregate temperature change = max(1,5) = 5. =
'''
#Python Solution : O(N), Space: O(1)

def aggregateTempChange(tempChange, n):
    maximum = float('-inf')
    for i in range(n):
        part1 = sum(tempChange[:i+1])
        part2 = sum(tempChange[i:])
        m = max(part1,part2)
        if m > maximum:
            maximum = m
    return maximum
out = aggregateTempChange([-1,2,3], 3)
print(out)
