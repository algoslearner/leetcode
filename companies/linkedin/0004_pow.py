'''
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
'''

# TC : O(N)
# SC : O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        
        N = n
        if(N < 0): N = -N   
        while(N > 0):
            #If it is an odd number, multiply ans by x, decrease N by 1
            if(N % 2 == 1): 
                ans = ans*x
                N = N-1
            #If it is an even number, square x, divide N by 2
            else: 
                x = x*x
                N = N/2
        
        #If it was negative, invert it (since it is to a negative power)
        if(n <0): 
            ans = 1 / ans
        return ans
