# https://leetcode.com/problems/most-frequent-subtree-sum/
'''
508. Most Frequent Subtree Sum

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

 

Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:


Input: root = [5,2,-5]
Output: [2]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
'''

####################################################################################################
# HASHMAP
# https://leetcode.com/problems/most-frequent-subtree-sum/discuss/98675/JavaC%2B%2BPython-DFS-Find-Subtree-Sum
'''
Use a hashMap count to count the subtree sum occurrence.

A sub function dfs(TreeNode node) will
travel through a tree, recursively calculate the sum of subtree,
increment the count, and finally return the sum of the sub tree.
'''

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []

        def dfs(node):
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = collections.Counter()
        dfs(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]
