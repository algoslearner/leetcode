# https://leetcode.com/problems/balance-a-binary-search-tree/
'''
1382. Balance a Binary Search Tree
Fb 11, google 2, amazon 6

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
'''

#############################################################################################################
# https://leetcode.com/problems/balance-a-binary-search-tree/discuss/540038/python-3-easy-to-understand
# TC: O(n log n)
# SC: O(n)

class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		v = []
		def dfs(node):
			if node:
				dfs(node.left)
				v.append(node.val)
				dfs(node.right)
		dfs(root)

		def bst(v):
			if not v:
				return None
			mid = len(v) // 2
			root = TreeNode(v[mid])
			root.left = bst(v[:mid])
			root.right = bst(v[mid + 1:])
			return root

		return bst(v)
  
####################################################################################################################
# Slicing will introduce extra space. Using indexes can reduce space complexity

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def in_order_traverse(root):
            if root is None:return
            in_order_traverse(root.left)
            nodes.append(root)
            in_order_traverse(root.right)
        
        def build_balanced_tree(left, right):
            if left>right:return None
            mid = (left+right)//2
            root = nodes[mid]
            root.left = build_balanced_tree(left, mid-1)
            root.right = build_balanced_tree(mid+1, right)
            return root
          
        in_order_traverse(root)
        return build_balanced_tree(0, len(nodes)-1)
