####################################################################################################
# Amazon OA question: https://leetcode.com/discuss/interview-question/1858858/amazon-oa
# https://leetcode.com/discuss/interview-question/1978286/Amazon-oror-OA-oror-Find-Earliest-Month-Stock-Problem-oror-24th-April-2022
####################################################################################################

'''
The interns at Amazon were asked to review the company's stock value over a period. Given the stock prices of n months, the net price change for the ith month is defined as the absolute difference between the average of stock prices for the first i : months and for the remaining (n - i) months where 1 si<n. Note that these averages are rounded down to an integer.

Given an array of stock prices, find the month at which the net price change is minimum. If there are several such months, return the earliest month.

Note: The average of a set of integers here is defined as the sum of integers divided by the number of integers, rounded down to the nearest integer. For example, the average of [1, 2, 3, 4] is the floor of (1 + 2+ 3+ 4)/4= 2.5 and the floor of 2.5 is 2.

Example :

stockPrice = [1, 3, 2, 4,5]
answer : 2

stockPrice = [1,1,1,1,1,1]
answer : 1

Solution : (15/15) ALL TEST CASES PASSED
'''

def findEarliestMonth(stockPrice):
    optimalMonth=0
    price=float('inf')
    totalSum=sum(stockPrice)
    total=0
    n=len(stockPrice)
    for month,value in enumerate(stockPrice,start=1):
        if(month==n):
            break
        total+=value
        k=total//month
        p=(totalSum-total)//(n-month)
        net=abs(k-p)
        if(net<price):
            price=net
            optimalMonth=month
    return optimalMonth

##########################################################################################
# BACKUP SOLUTIONS LISTED
##########################################################################################

#initialize month variable with 0
    month=0
    change=max(stockPrice)
    #Create a list to hold values
    l=[]
    total_sum = 0
    for i in range(len(stockPrice)):
        total_sum+=stockPrice[i]
    left = 0
    left_sum = 0
    while(len(stockPrice)>1):
        left = stockPrice.pop(0)
        l.append(left)
        #Now calculate the average
        left_sum += left
        avg1=left_sum //len(l)
        avg2=(total_sum-left_sum)//len(stockPrice)
        
        if(abs(avg1-avg2)
           
           
# Related leetcode question: There is a question using the same concept here: 238. Product of Array Except Self
# The result is just a formula: min(abs(avg(0,i) - avg(i+1,n-1))) where 0 <= i < n
# And share my Java solution:
# time: O(n), space: O(1)
           
int minumumNetPriceMonth(int[] prices) {
    int n = prices.length, sum = 0, min = Integer.MAX_VALUE, res = 0;
    for (int price : prices) {
        sum += price;
    }
    int presum = 0;
    for (int i = 0; i < n; i++) {
        presum += prices[i];
        int avg1 = presum / (i + 1);
        int avg2 = i == n - 1 ? 0 : (sum - presum) / (n - i - 1);
        int net = Math.abs(avg1 - avg2);
        if (net < min) {
            res = i + 1;
            min = net;
        }
    }
    return res;
}
