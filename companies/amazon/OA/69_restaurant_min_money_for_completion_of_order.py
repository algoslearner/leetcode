# https://leetcode.com/discuss/interview-question/1793937/Amazon
'''
Problem statement
You are the owner of a restaurant. On a particular day, there are N orders coming in. The billing policy for each order is as follows:

For each minute of preparation of the order, the cost is K units of money.
For each minute when an order has been received, but its preparation has not been started, W units of money is discounted.
The chef in the restaurant believes that it is most profitable if he follows the following rules to select the sequence in which he prepares the orders:

If no order is being prepared, start preparing the order that has the least preparation time from among the pending orders.
If there are two or more pending orders having the same preparation time, pick the order that was received first.
If the waiting discount is greater than the cost of preparation, the order is considered to be free which means, money earned is 0.
Task
Determine the money earned for the completion of each order.

Assumptions

N = 4
K = 5
W = 1
each-order has [x,y] where x is the start time of the order and y is the preparation of the order.
Example:
orders = [[1,4],[2,2],[3,3],[9,1]]
Output -> [20,7,13,5] -
[1,4] (1 is the start time,4 is the processing time)-> 20
As its a first job and no need to wait. and the cost would be is * 5-1 * 0(4 is the processing time taken,5 is the cost for every processing minute,1 is the cost for every wait minute,0 as its not waiting for any order)
[2,2]-> 7 as it needs to wait till 5sec(1+4) -> 5 * 2-3 * 1
[3,3] 13 as it needs to wait till 5sec(1+4)-> 5 * 3-2 * 1
[9,1] 5 no need to wait -> 5 * 1-0

This will be solved using priority queues based on the completion time.
but how to solve the use-case of "If no order is being prepared, start preparing the order that has the least preparation time from among the pending orders."

priority queues
'''
