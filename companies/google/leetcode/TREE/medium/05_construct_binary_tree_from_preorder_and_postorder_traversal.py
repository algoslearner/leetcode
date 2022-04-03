'''
Given two integer arrays, preorder and postorder where 
preorder is the preorder traversal of a binary tree of distinct values and 
postorder is the postorder traversal of the same tree, 
reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#################################################################################################
# EASIER RECURSION
# TC: O(N)
# SC: O(N)
'''
# The first element in "pre" and the last element in "post" should both be the value of the root. 
# The second to last of "post" should be the value of right child of the root. 
# So we can find the index to split "left" and "right" children in "pre". 
# Don't forget to evaluate if the length of "post" is larger than 1, since we used post[-2].
'''

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder: return None
        root = TreeNode(preorder[0])
        if len(postorder) == 1: return root
        
        idx = preorder.index(postorder[-2])
        root.left = self.constructFromPrePost(preorder[1: idx], postorder[:(idx - 1)])
        root.right = self.constructFromPrePost(preorder[idx: ], postorder[(idx - 1):-1])
        return root

#################################################################################################
# RECURSION
# TC: O(N)
# SC: O(N)
'''
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)
Complexity:
Time O(N), as we iterate both pre index and post index only once.
Space O(height), depending on the height of constructed tree.


Recursive Solution
Create a node TreeNode(pre[preIndex]) as the root.

Becasue root node will be lastly iterated in post order,
if root.val == post[posIndex],
it means we have constructed the whole tree,

If we haven't completed constructed the whole tree,
So we recursively constructFromPrePost for left sub tree and right sub tree.

And finally, we'll reach the posIndex that root.val == post[posIndex].
We increment posIndex and return our root node.

# explanation diagrams: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/821268/C-Construct-tree-using-preorder-traversal-first
'''

class Solution:
    preIndex, posIndex = 0, 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1
        if (root.val != postorder[self.posIndex]):
            root.left = self.constructFromPrePost(preorder, postorder)
        if (root.val != postorder[self.posIndex]):
            root.right = self.constructFromPrePost(preorder, postorder)
        self.posIndex += 1
        return root
      
#################################################################################################
# ITERATION
# TC: O(N)
# SC: O(N)

def constructFromPrePost(self, pre, post):
        stack = [TreeNode(pre[0])]
        j = 0
        for v in pre[1:]:
            node = TreeNode(v)
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
