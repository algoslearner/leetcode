# Question screenshot: https://leetcode.com/discuss/interview-question/378221/Twitter-or-OA-2019-or-Final-Discounted-Price
# https://leetcode.com/discuss/interview-question/985908/Amazon-or-OA-2020-or-Shopkeeper-Sale
'''
A shopkeeper has a sale to complete and has arranged the items being sold in a list.
Starting from the left, the shop keeper rings up each item at its full price less the price of the first lower or equally priced item to its right.
If there is no item to the right that costs less than or equal to the current item's price the current item is sold at full price.
Assumptions
The first and second items would each be discounted by 1 unit, the first equal or lower price to the right.
The item priced 1 unit would sell at a full price.
The next item, at 2 units, would be discounted 2 units as would the 4 unit item.
The sixth and final item must be purchased at full price.
Input
The input consists of one arguments:
items_prices : a list of integers representing the price of items
Output
return total cost of all items on the first line and on the second line print a space separated list of integers representing the indexes of the non- discounted items in ascending index order.
Constraints
1 <= size(prices) <= 100000
1 <= prices <= 1000000
Examples
Example 1:
Input:
items_prices = [2, 3, 1, 2, 4, 2]
Output:
18
2 5
Explanation:
The total cost is 1+2+1+0+2+2 = 8 units. And 2 and 5 indexes has no discount.
Examples
Example 2:
Input:
items_prices = [5, 1, 3, 4, 6, 2]
Output:
14
1 5
Examples
Example 3:
Input:
items_prices = [1, 3, 3, 2, 5]
Output:
9
0 3 4

public static List<List> shopkeeperSale(int[] items_prices){
'''

########################################################################################################
# MONOTONIC STACK
'''
if it helps someone, you can understand the mechanics behind the solution for this question by going through this question: https://leetcode.com/problems/largest-rectangle-in-histogram/ (very similar). the linear solution uses "monotonic stacks".

there's a very good blog on monotonic stacks here: https://medium.com/techtofreedom/algorithms-for-interview-2-monotonic-stack-462251689da8

python O(n) solution:
'''

from collections import deque

def finalDiscountedPrice(prices):
    # start creating a monotonic stack from the first element
    # the moment a smaller element or equal is found than the last one added to the stack
    # that element will be the subtractor of all the elements of the stack which are more than it
    # since it will be the first smaller element for the monotonically increasing elements more than it
    # just before it

    prices += [0]
    mono_stack = deque()
    result = deque()
    unchanged = []

    for i, p in enumerate(prices):
        if not mono_stack or p > prices[mono_stack[0]]:
            mono_stack.appendleft(i)
        else:
            stack_result = deque()
            while mono_stack and prices[mono_stack[0]] >= p:
                popped = mono_stack.popleft()
                stack_result.appendleft(prices[popped] - p)
                if stack_result[0] == prices[popped]:
                    unchanged.append(popped)
            result += list(stack_result)
            mono_stack.appendleft(i)

    return sum(result), list(reversed(unchanged))

if __name__ == '__main__':
    print(finalDiscountedPrice([2,3,1,2,4,2])) # output: 8 .. [2, 5]
    print(finalDiscountedPrice([5, 1, 3, 4, 6, 2]))  # output: 14 .. [1, 5]
    # [4, 1, 1, 2, 4, 2 ]
    print(finalDiscountedPrice([1, 3, 3, 2, 5]))  # output: 9 .. [0, 3, 4]
    # [1, 0, 1, 2, 5]
    print(finalDiscountedPrice([1, 3, 4, 3, 2, 5]))  # output: 11 .. [0, 4, 5]
    # [1, 0, 1, 1, 2, 5]
    print(finalDiscountedPrice([1, 7, 4, 6, 2, 5]))  # output: 17 .. [0, 4, 5]
    # [1, 3, 2, 4, 2, 5]
    print(finalDiscountedPrice([5, 15, 27, 34, 3, 2, 1, 4, 6, 2]))  # output: 80 .. [6, 9]
