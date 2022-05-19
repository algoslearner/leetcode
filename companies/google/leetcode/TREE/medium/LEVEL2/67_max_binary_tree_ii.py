# https://leetcode.com/problems/maximum-binary-tree-ii/
'''
998. Maximum Binary Tree II

A maximum tree is a tree where every node has a value greater than any other value in its subtree.

You are given the root of a maximum binary tree and an integer val.

Just as in the previous problem, the given tree was constructed from a list a (root = Construct(a)) recursively with the following Construct(a) routine:

If a is empty, return null.
Otherwise, let a[i] be the largest element of a. Create a root node with the value a[i].
The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]).
The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]).
Return root.
Note that we were not given a directly, only a root node root = Construct(a).

Suppose b is a copy of a with the value val appended to it. It is guaranteed that b has unique values.

Return Construct(b).

 

Example 1:


Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: a = [1,4,2,3], b = [1,4,2,3,5]
Example 2:


Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: a = [2,1,5,4], b = [2,1,5,4,3]
Example 3:


Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: a = [2,1,5,3], b = [2,1,5,3,4]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 100
All the values of the tree are unique.
1 <= val <= 100
'''

##################################################################################################
# RECURSION
# TC: O(N)
# SC: O(N), recursion stack

# https://leetcode.com/problems/maximum-binary-tree-ii/discuss/242936/JavaC%2B%2BPython-Recursion-and-Iteration
# If root.val > val, recursion on the right.
# Else, put right subtree on the left of new node TreeNode(val)

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node
      
##################################################################################################
# Iteration
# TC: O(N)
# SC: O(1)

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pre,cur = None, root
        while cur and cur.val > val:
            pre, cur = cur, cur.right
        node = TreeNode(val)
        node.left = cur
        if pre: pre.right = node
        return root if root.val > val else node
 
##################################################################################################
'''
For any one who can't understand the question. I give my explanation.

1. the given tree was constructed from an list A (root = Construct(A)). So, List A = new ArrayList();
2. Suppose B is a copy of A with the value val appended to it. So, B = new ArrayList(A) and B.add(val);
3. The left child of root will be Construct([A[0], A[1], ..., A[i-1]]),
    The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]]).
    in this case A represent B, B[B.length-1] = val, So.
4. If val is the largest, i = B.length-1, the root node's value is val, i=0 to i-1 are in the left child of root.
    This explains why when val > root.val, root should be the left child of new node with value val.
5. Else val is not the largest, the new node with value val is always the right child of root.
'''
