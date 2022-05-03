# https://leetcode.com/problems/deepest-leaves-sum/
'''
1302. Deepest Leaves Sum

Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
'''

#########################################################################################
# ITERITIVE BFS
# TC: O(n)
# SC: O(1)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        next_level = deque([root,])
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()
            
            for node in curr_level:
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        
        return sum([node.val for node in curr_level])
      
#########################################################################################
# Iterative DFS
# TC: O(n)
# SC: O(h)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_sum = depth = 0
        stack = [(root, 0) ]
        
        while stack:
            node, curr_depth = stack.pop()
            if node.left is None and node.right is None:
                # if this leaf is the deepest one seen so far
                if depth < curr_depth:
                    deepest_sum = node.val      # start new sum
                    depth = curr_depth          # note new depth
                # if there were already leaves at this depth
                elif depth == curr_depth:
                    deepest_sum += node.val     # update existing sum
                    
            else:
                if node.right:
                    stack.append((node.right, curr_depth + 1))
                if node.left:
                    stack.append((node.left, curr_depth + 1))
                        
        return deepest_sum
      
#########################################################################################
# Recursion
# TC: O(n)
# SC: O(h)

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def preorder(node = root, depth = 0):
            nonlocal maxd, total
            if not node:
                return
            if depth > maxd:
                maxd = depth
                total = 0
            if depth == maxd:
                total += node.val
            preorder(node.left, depth+1)
            preorder(node.right, depth+1)
        
        maxd, total = -1, 0
        preorder()
        return total
