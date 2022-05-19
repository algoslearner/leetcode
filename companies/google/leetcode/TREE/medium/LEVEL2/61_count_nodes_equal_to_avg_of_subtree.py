# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
'''
2265. Count Nodes Equal to Average of Subtree

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
 

Example 1:


Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
Example 2:


Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
'''

##########################################################################################################
# DFS + preorder traversal
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/discuss/2018193/Python-or-DFS(Preorder-Traversal)
'''
Our goal is to iterate each and every node by using any kind of traversal technique (preorder, postorder, inorder). (I have used preorder here),

For every node, we calculate the sum of its subtree nodes and keep a variable to store the no. of nodes,
so that we can calculate average by total sum/ total nodes.

If our average is equal to value of the root, we increment the count.
'''

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        def calculate_average(root):
            if root:
                self.summ += root.val
                self.nodecount += 1
                calculate_average(root.left)
                calculate_average(root.right)
        
        
        def calculate_for_each_node(root):
            if root:
                self.summ = 0
                self.nodecount = 0
                calculate_average(root)
                if ((self.summ) // (self.nodecount)) == root.val:
                    self.count += 1 
                calculate_for_each_node(root.left)
                calculate_for_each_node(root.right)
                
                
        self.count = 0
        calculate_for_each_node(root)       
        return self.count
