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

class Solution:
    def numSquares(self, n: int) -> int:
        
        # MATH : four-square theorem
        # TC : O(n^0.5)
        # SC : O(1)
        
        while( n % 4 == 0 ):
            # Reduction by factor of 4
            n //= 4
            
        if n % 8 == 7:
            # Quick response for n = 8k + 7
            return 4
        
        # Check whether n = a^2 + b^2
        for a in range( int(sqrt(n))+1 ):
            
            b = int( sqrt( n - a*a ) )
            
            if ( a**2 + b ** 2 ) == n :
                return (a>0) + (b>0)
            
        # n = a^2 + b^2 + c^2
        return 3
        
############################################################################
#### BFS


class Solution:
    def numSquares(self, n: int) -> int:
        
        # BFS
        # TC : O(n)
        # SC : O(n)
        
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        d = 1 
        q = {n} 
        nq = set()
	    
        while q:
            for node in q:
                for square in squares:
                    if node == square: return d
                    if node < square: break
                    nq.add(node-square)
            q, nq, d = nq, set(), d+1
        
        
