# https://leetcode.com/problems/sum-of-left-leaves/
'''
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
'''

########################################################################################
# RECURSION
# TC: O(n)
# SC: O(n)

class Solution:
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def process_subtree(subtree, is_left):
            
            # Base case: If this subtree is empty, return 0
            if subtree is None:
                return 0
            
            # Base case: This is a leaf node.
            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0
            
            # Recursive case: return result of adding the left and right subtrees.
            return process_subtree(subtree.left, True) + process_subtree(subtree.right, False)

        return process_subtree(root, False)
      
########################################################################################
# ITERATION
# TC: O(n)
# SC: O(n)

class Solution:
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if root is None: 
            return 0

        def is_leaf(node):
            return node is not None and node.left is None and node.right is None

        stack = [root]
        total = 0
        while stack:
            sub_root = stack.pop()
            # Check if the left node is a leaf node.
            if is_leaf(sub_root.left):
                total += sub_root.left.val
            # If the right node exists, put it on the stack.
            if sub_root.right is not None:
                stack.append(sub_root.right)
            # If the left node exists, put it on the stack.
            if sub_root.left is not None:
                stack.append(sub_root.left)

        return total
      
########################################################################################
# MORRIS
# TC: O(n)
# SC: O(1)

class Solution:
    
    def sumOfLeftLeaves(self, root):
        total_sum = 0
        current_node = root
        while current_node is not None:
            # If there is no left child, we can simply explore the right subtree
            # without needing to worry about keeping track of currentNode's other
            # child.
            if current_node.left is None: 
                current_node = current_node.right 
            else: 
                previous = current_node.left 
                # Check if this left node is a leaf node.
                if previous.left is None and previous.right is None:
                    total_sum += previous.val
                # Find the inorder predecessor for currentNode.
                while previous.right is not None and previous.right is not current_node:
                    previous = previous.right
                # We've not yet visited the inorder predecessor. This means that we 
                # still need to explore currentNode's left subtree. Before doing this,
                # we will put a link back so that we can get back to the right subtree
                # when we need to.
                if previous.right is None:
                    previous.right = current_node  
                    current_node = current_node.left  
                # We have already visited the inorder predecessor. This means that we
                # need to remove the link we added, and then move onto the right
                # subtree and explore it.
                else:
                    previous.right = None
                    current_node = current_node.right
        return total_sum
