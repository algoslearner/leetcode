# https://leetcode.com/problems/candy/
'''
135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''

###############################################################################################################################################
# two pass - left to right and right to left
# TC: O(n)
# SC: O(1)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        # Concept - Just do what the problem is saying, we can 
        # fill our result array with one, now the first requirement
        # is fulfilled and for 2nd requirement, there will be 2 cases
        # 1 - Rating at i is greater than at i-1 --> Forward Pass
        # 2 - Rating at i is greater than i + 1 --> Backward Pass
        
        
        # Condition-1 Fulfilled as we gave 1 candy to everyone
        candies = [1] * len(ratings)
        
        # Calculate the candies needed to fulfill left condition     
        # We drop the 0th element as nothing is located left to it
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # Calculate the candies needed to fulfill right condition  
        # We drop the last element as nothing is located right to it
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        # Take the summation --> Minimum candies
        return sum(candies)
