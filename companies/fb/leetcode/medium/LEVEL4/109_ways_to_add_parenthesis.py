'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
'''

# https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/866096/Python%3A-Divde-and-Conquer-%2B-Memoization-%2B-O(N-*-2N)
###########################################################################################################################################
'''
Time Complexity: O(N * 2^N)
Let N be the length of the expression
In the worst case there are N // 2 operations: when all expression numbers are numbers of 1 digits
For example, expression: 1+2+3+4+5+6
len(expression) = 11
operations # = 5
Therefore, our recursion depth is O(N/2)
		depth         Nbr of problem           work at corresponding depth
		0             1                        O(N) #divide expression
		1             2                        O(1) + O(N - 2) = O(N) * 2
		...
		i             2^i                      O(N) * 2^i 
		...
		N//2          2^N//2                   O(N) * 2^N//2

		Total time complexity: O(N) (2^0 + 2^1 + ... + 2^N//2) = O(N * 2^N//2) = O(N * 2^N)
	    
Final notes:
- This problem is similar to 22. Generate Parentheses problem
- Check its solution for more accurate time complexity
'''

class Solution:
    def __init__(self):
	    self.operation = {}
	    self.operation['*'] = lambda a, b: a * b
	    self.operation['+'] = lambda a, b: a + b
	    self.operation['-'] = lambda a, b: a - b

    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        return self.evaluate_expression(expression, {})

    def evaluate_expression(self, expression: str, memo: dict) -> List[int]:
        if expression in memo:
            return memo[expression]
        
        if expression.isnumeric():
            return [int(expression)]
        
        results = []
        for i in range(len(expression)):
            if expression[i] not in self.operation:
                continue
                
            opr = expression[i]

		    # Divide:
            left_results = self.diffWaysToCompute(expression[0:i])
            right_results = self.diffWaysToCompute(expression[i+1:])
            
            for left in left_results: # Conquer:
                for right in right_results:
                    results.append(self.operation[opr](left, right))
                    
        memo[expression] = results
        return results  
        
