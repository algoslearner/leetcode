'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Accepted
696,869
Submissions
1,302,219
'''

# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        level = 0 # to track the level on which we are currently
        
        dict_level = defaultdict(deque)
        # deque for performing bfs
        dq = deque([root])
        
        while dq:
            level_size = len(dq)
            for i in range(level_size): # until the current level size
                node = dq.popleft() # we pop from the left of dq
                # if we are at level number which is odd, we will 
                # appendleft the values in deque for that level
                if (level%2 == 1):
                    dict_level[level].appendleft(node.val)
                # Otherwise we will append at right
                else:
                    dict_level[level].append(node.val)
                # put the left and right child nodes in the queue
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            # increment the level when we are finished with current level
            level += 1 
        
        # now the dictionary values are the list that contains the zigzag traversal that we want to see
        return dict_level.values()
        
