# https://leetcode.com/problems/climbing-stairs/
'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

'''
Similar questions:
91. Decode Ways
62. Unique Paths
509. Fibonacci Number

Practice them in a row for better understanding 
'''

#########################################################################################################################
# DP
# TC: O(n)
# SC: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2: return n
        
        current = 0
        prev1 = 1
        prev2 = 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current
        
#########################################################################################################################
# optimized - math
# TC: O( log n)
# SC: O(1)


public class Solution {
    public int climbStairs(int n) {
        double sqrt5 = Math.sqrt(5);
        double phi = (1 + sqrt5) / 2;
        double psi = (1 - sqrt5) / 2;
        return (int) ((Math.pow(phi, n + 1) - Math.pow(psi, n + 1)) / sqrt5);
    }
}

########################################################################################################################
# Logic
'''
Think about what happens on the n-th step. You can get to it either from (n - 1) step, or from (n - 2) step.
Say there are x distinct ways to get to (n - 1) step, and y distinct ways to get to (n - 2) step.

For (n - 1), to get to n you just need to add 1 to the end of each of those x paths that lead here.
That does not change the number of those paths in which we're interested -- it just makes them all acquire a 'tail' of 1.

For (n - 2), to get to n you will need to add 2 to each of the y paths that lead there.
That also doesn't change the number of the paths that lead to it, just makes them all acquire a 'tail' of 2.

What actually happens at the step of n, is you adding up those two groups of possible ways to get to n.

Let's do an example to make it more clear. Say n = 5. You can get to 5 either from 3 or from 4.

Let's think about all the paths that lead to 3. Here they are:

[1 + 1 + 1]
    [2 + 1]
    [1 + 2]
To get to 5 from all of them, you just need to add 2 to the end of each path:

[1 + 1 + 1] + 2
    [2 + 1] + 2
    [1 + 2] + 2
See how the number of ways to get from 3 to 5 does not change with this operation? You're adding 2 to each sequence, but that is just making each sequence longer, not making more of possible sequences.

Similarly, for 4 we have those five possible ways to get to it:

[1 + 1 + 1 + 1]
    [1 + 1 + 2]
    [1 + 2 + 1]
    [2 + 1 + 1]
        [2 + 2]
To get to 5 from that you're adding 1 in the end of each, so we'll have:

[1 + 1 + 1 + 1] + 1
    [1 + 1 + 2] + 1
    [1 + 2 + 1] + 1
    [2 + 1 + 1] + 1
        [2 + 2] + 1
See how that also doesn't change the number of ways we got here in any way.

So the total number of paths to get to 5 is all the paths to get to 3, and all the paths to get to 4:

    [1 + 1 + 1] + 2
        [2 + 1] + 2
        [1 + 2] + 2
[1 + 1 + 1 + 1] + 1
    [1 + 1 + 2] + 1
	[1 + 2 + 1] + 1
	[2 + 1 + 1] + 1
	    [2 + 2] + 1
Hope it makes sense.
'''
