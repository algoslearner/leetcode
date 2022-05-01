# https://leetcode.com/problems/construct-string-from-binary-tree/
'''
606. Construct String from Binary Tree

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 

Example 1:


Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:


Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

######################################################################################################
# RECURSION
# TC: O(n)
# SC: O(n)

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        elif not root.left and not root.right:
            return str(root.val) + ""
        elif not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        else:
            return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
          
 
######################################################################################################
# RECURSION optimizing string creation
# TC: O(n)
# SC: O(n)

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        ans=[]
        def h(node):
            if not node:
                return ans
            ans.append(str(node.val))
            if(node.left is None and node.right is not None):
                ans.append('()')
            if(node.left):
                ans.append('(')
                h(node.left)
                ans.append(')')
            if(node.right):
                ans.append('(')
                h(node.right)
                ans.append(')')
            return ans
        h(root)
        return "".join(ans)
      
########################################################################################################
# Iteration
# TC: O(n)
# SC: O(n)
# https://leetcode.com/problems/construct-string-from-binary-tree/discuss/279009/Python-O(N)-Iterative-PrePost-Order-BST-Traversal

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        output = []
        
        stack = [root]
        while stack:
            node = stack.pop()
            if type(node) is str:
                output.append(node)
            else:
                output.append("(")
                output.append(str(node.val))
                stack.append(")")
                
                if node.right: stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
                elif node.right:
                    stack.append("()")
                    
        return "".join(output[1:-1])
