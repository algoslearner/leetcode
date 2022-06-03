# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
'''
272. Closest Binary Search Tree Value II

Given the root of a binary search tree, a target value, and an integer k, 
return the k values in the BST that are closest to the target. 

You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104.
0 <= Node.val <= 109
-109 <= target <= 109
 

Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?
'''

'''
class TreeNode:
    def __init__(val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
'''

###############################################################################################################################
# recursive inorder + sort
# TC: O(N log N)
# SC: O(N)

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(root: TreeNode) -> List[int]:
            if root:
                return inorder(root.left) + [root.val] + inorder(root.right)
            else:
                return []
        
        nums = inorder(root)
        nums.sort(key = lambda x: abs(x - target))
        return nums[:k]
      
###############################################################################################################################
# recursive inorder + heap (Facebook friendly)
# TC: O(N log k)
# SC: O(k + H)

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def inorder(node: TreeNode):
            if not node:
                return
            
            inorder(node.left)
            diff = abs(node.val - target)
            heapq.heappush(maxheap, [-diff, node.val])
            if len(maxheap) > k:
                heapq.heappop(maxheap)   
            inorder(node.right)
        
        maxheap = []
        inorder(root)
        return [x for _, x in maxheap]
      
      
###############################################################################################################################
# quick select (google friendly)
# TC: O(N), worst case i O(N^2), although the chance of getting worst case is negligible
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def partition(self, pivot_idx: int, left: int, right: int) -> int:
            pivot_dist = self.dist(pivot_idx)
            
            # 1. move pivot to end
            self.nums[right], self.nums[pivot_idx] = self.nums[pivot_idx], self.nums[right]
            store_idx = left
            
            # 2. move more close elements to the left
            for i in range(left, right):
                if self.dist(i) < pivot_dist:
                    self.nums[i], self.nums[store_idx] = self.nums[store_idx], self.nums[i]
                    store_idx += 1
                    
            # 3. move pivot to its final place
            self.nums[right], self.nums[store_idx] = self.nums[store_idx], self.nums[right]
            return store_idx
        
    def quickselect(self, left: int, right: int) -> None:
        # base case: list contains only one element
        if left == right:
            return
        
        # select a random pivot index
        pivot_idx = randint(left, right)
        # find the pivot position in sorted list
        true_idx = self.partition(pivot_idx, left, right)
        
        # if the pivot is in its final sorted position
        if true_idx == self.k:
            return
        elif true_idx < self.k:
            # go left
            self.quickselect(true_idx, right)
        else:
            # go right
            self.quickselect(left, true_idx)
            
        
    def inorder(self, node: TreeNode) -> List[int]:
        if node:
            return self.inorder(node.left) + [node.val] + self.inorder(node.right)
        else:
            return []
        
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.k = k
        self.nums = self.inorder(root)
        self.dist = lambda i : abs(self.nums[i] - target)
        self.quickselect(0, len(self.nums) - 1)
        return self.nums[:k]
    
    
