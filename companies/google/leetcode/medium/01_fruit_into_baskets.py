'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
'''

###############################################################################################
# Sliding window, with hashmap to track count of 2
# TC: O(N)
# SC : O(1), hashmap with two values is O(1)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # corner case: small array
        n = len(fruits)
        if n < 3:
            return n
        
        # sliding window
        left = 0
        right = 0
        maxlen = 2
        hashmap = {}
        
        while right < n:
            hashmap[fruits[right]] = right
            right += 1
            
            if len(hashmap) == 3:
                minindex = min(hashmap.values())
                del hashmap[fruits[minindex]]
                
                left = minindex + 1
            
            maxlen = max(maxlen, right-left)
        return maxlen
