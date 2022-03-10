'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''

'''
Solution 1. According to Lagrange's four-square theorem(please wiki/google), any positive number can be represented as 4(at most) square number sum.

divide by 4, notice that, 2 and 8, 3 and 12, 4 and 16 has the same number of square factors.
if number%8==7, this result in a square factors 2^2 + 1 +1 +1, which is four.
if any two numbers can suqare sum to n, return 1 or 2.
otherwise result is 3.
'''

Solution 1. According to Lagrange's four-square theorem(please wiki/google), any positive number can be represented as 4(at most) square number sum.

divide by 4, notice that, 2 and 8, 3 and 12, 4 and 16 has the same number of square factors.
if number%8==7, this result in a square factors 2^2 + 1 +1 +1, which is four.
if any two numbers can suqare sum to n, return 1 or 2.
otherwise result is 3.

public class Solution {
    public int numSquares(int n) {
        while(n%4 == 0)  n /= 4;
        if(n%8 == 7) return 4;
        for(int x=0; x*x <=n; x++){
            int y = (int)Math.sqrt(n - x*x);
            if(x*x + y*y == n){
                if(x == 0 || y == 0) return 1;
                else return 2;
            }
        }
        return 3;
    }
}
Solution 2. recusive.

public class Solution {
    public int numSquares(int n) {
        int res = n, num =2;
        while(num * num <=n){
            int x = n/(num*num), y = n%(num*num);
            res = Math.min(res, x + numSquares(y));
            ++num;
        }

        return res;
    }
}
Solution 3. DP. this is a forward dp question, using an array dp[], dp[i] means the number need to square-sum up to i, then, for all the j from 1 to i+jj <=n; calculate dp[i+jj] = ?, initially set each dp[i] equals to max.

public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        for(int i=1; i<=n; i++){
            dp[i] = Integer.MAX_VALUE;
        }
        dp[0]=0;
        for(int i=0; i<=n; i++){
            for(int j=1; i+ j*j <=n; j++){
                dp[i+j*j] = Math.min(dp[i+j*j], dp[i]+1);
            }
        }

        return dp[n];
    }
}
