# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/
'''
1612. Check If Two Expression Trees are Equivalent

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the '+' operator (i.e. addition).

You are given the roots of two binary expression trees, root1 and root2. Return true if the two binary expression trees are equivalent. Otherwise, return false.

Two binary expression trees are equivalent if they evaluate to the same value regardless of what the variables are set to.

 

Example 1:

Input: root1 = [x], root2 = [x]
Output: true
Example 2:



Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,c]
Output: true
Explaination: a + (b + c) == (b + c) + a
Example 3:



Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,a,b,d]
Output: false
Explaination: a + (b + c) != (b + d) + a
 

Constraints:

The number of nodes in both trees are equal, odd and, in the range [1, 4999].
Node.val is '+' or a lower-case English letter.
It's guaranteed that the tree given is a valid binary expression tree.
 

Follow up: What will you change in your solution if the tree also supports the '-' operator (i.e. subtraction)?
'''


# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##############################################################################################################
# DFS + follow up
# TC: O(N)
# SC: O(log N)
# https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/discuss/884387/Python-simple-DFS-solution-and-follow-up
'''
Idea
We can use a dictionary to keep track of each value.
When traverse the first tree, we do dic[node.val] += 1. And when traverse the second tree, we do dic[node.val] -= 1. If two trees are equivalent, all dic values should be 0 at the end.
This method extends nicely to the follow-up question. If there's a minus sign, we simply revert the increment value (sign) of the right child.
'''

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        dic = collections.Counter()
        
        def dfs(node, sign):
            if not node:
                return
            if node.val == '+':
                dfs(node.left, sign)
                dfs(node.right, sign)
            elif node.val == '-': # for follow-up
                dfs(node.left, sign)
                dfs(node.right, -sign)
            else:
                dic[node.val] += sign
        
        dfs(root1, 1)
        dfs(root2, -1)
        return all(x == 0 for x in dic.values())
