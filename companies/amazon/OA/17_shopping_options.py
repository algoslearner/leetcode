# https://leetcode.com/discuss/interview-question/1031663/Amazon-OA
'''
Disappeared shopping options question, retrieved from google cache

A customer wants to buy a pair of jeans, a pair of shoes, a skirt, and a top but has a limited budget in dollars. Given different pricing options for each product, determine how many options our customer has to buy 1 of each product. You cannot spend more money than the budgeted amount.

Example
priceOfJeans = [2, 3]
priceOfShoes = [4]
priceOfSkirts = [2, 3]
priceOfTops = [1, 2]
budgeted = 10

The customer must buy shoes for 4 dollars since there is only one option. This leaves 6 dollars to spend on the other 3 items. Combinations of prices paid for jeans, skirts, and tops respectively that add up to 6 dollars or less are [2, 2, 2], [2, 2, 1], [3, 2, 1], [2, 3, 1]. There are 4 ways the customer can purchase all 4 items.

Function Description

Complete the getNumberOfOptions function in the editor below. The function must return an integer which represents the number of options present to buy the four items.

getNumberOfOptions has 5 parameters:
int[] priceOfJeans: An integer array, which contains the prices of the pairs of jeans available.
int[] priceOfShoes: An integer array, which contains the prices of the pairs of shoes available.
int[] priceOfSkirts: An integer array, which contains the prices of the skirts available.
int[] priceOfTops: An integer array, which contains the prices of the tops available.
int dollars: the total number of dollars available to shop with.

Constraints

1 ≤ a, b, c, d ≤ 103
1 ≤ dollars ≤ 109
1 ≤ price of each item ≤ 109
Note: a, b, c and d are the sizes of the four price arrays
'''
# Solution idea: https://github.com/phoenix-254/Amazon-OA/blob/main/shopping_options.java

# its actually a 3sum problem
# Shopping Option Amazon OA Question Similar to 4 Sum II problem: https://leetcode.com/problems/4sum-ii/

###############################################################################################
# TC: O(N^3)
# TLE
# This is also too slow, as it's a O(n^3) time complexity solution so some of the test cases will result in TLE. 

def shoppingOptions(pairOfJeans, pairOfShoes, pairOfSkirts, pairOfTops, dollars):
    """
    :type pairOfJeans: List[int]
    :type pairOfShoes: List[int]
    :type pairOfSkirts: List[int]
    :type pairOfTops: List[int]
    :type dollars: int
    :rtype: int
    """
    
    hash_map = {}
    count = 0
    
    for a in pairOfJeans:
        for b in pairOfShoes:
            curr_sum = a+b
            if curr_sum in hash_map:
                hash_map[curr_sum] += 1
            else:
                hash_map[curr_sum] = 1
            
    for c in pairOfSkirts:
        for d in pairOfTops:
            curr_val = dollars - (c + d)
            li_keys = [k for k in hash_map if k <= curr_val]
            values = [hash_map.get(k) for k in li_keys]
            count += sum(values)
            
    return count

print(shoppingOptions([2], [3, 4], [2, 5], [4, 6], 12)) # Ans 2
print(shoppingOptions([2], [2, 2], [2], [2], 9)) # Ans 2
print(shoppingOptions([4, 7], [6, 6], [1, 3, 5], [5, 7, 12], 20)) # Ans 12

###############################################################################################
# TC: O(N^2)
# When the target/dollars isn't exact, you'll need to store the first set of price counts in a dp table, and process that table dp[i+1] += dp[i], so you end up with a Time Complexity O(n^2) solution.

def shoppingOptions(pairOfJeans, pairOfShoes, pairOfSkirts, pairOfTops, dollars):
    dp = [0 for _ in range(dollars + 1)] # you can trim this too, looking at max/min pairs, but unnecessary.
    count = 0

    for a in pairOfJeans:
        for b in pairOfShoes:
            if 0 <= a + b <= dollars:
                dp[a+b] += 1

    for i in range(1, dollars+1):
        dp[i] += dp[i-1]
        
    for c in pairOfSkirts:
        for d in pairOfTops:
            if 0 <= dollars - (c + d) <= dollars:
                count += dp[dollars - (c + d)]
            
    return count
