'''
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.

 

Example 1:

Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Constraints:

n == ages.length
1 <= n <= 2 * 104
1 <= ages[i] <= 120
'''

# An easy-understood binary search solution. Find the lower bound and upper bound of a range where ages[i] can send request.
'''
Explanation
Write a sub function request(a, b) to check if age a will friend requests age b.
I just copy it from description:
return !(condition1 || condition2 || condition3)

Count nunmber of all ages to a map.
Because we have at most 20000 ages but only in range [1, 120].

For each age a and each age b != a, if request(a, b), we will make count[a] * count[b] requests.

For each age a, if request(a, a), we will make count[a] * (count[a] - 1) requests.
'''

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request(x, y):
            condition1 = (y <= 0.5 * x + 7)
            condition2 = (y > x)
            condition3 = (y > 100 and x < 100)
            return not (condition1 or condition2 or condition3)
        
        agesCount = collections.Counter(ages)
        requestsCount = 0
        for x in agesCount:
            for y in agesCount:
                if request(x,y):
                    requestsCount += agesCount[x] * (agesCount[y] - (x == y))
        return requestsCount
