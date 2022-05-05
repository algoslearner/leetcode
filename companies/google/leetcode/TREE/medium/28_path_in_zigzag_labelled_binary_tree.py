# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
'''
1104. Path In Zigzag Labelled Binary Tree
Fb 2

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
'''

##########################################################################################################
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-O(logn)-time-and-space-with-readable-code-and-step-by-step-explanation
# 1) You can easily determine the parent by dividing by 2 with a normally ordered (non-zigzag) binary tree
# 2) So we now how how to trace from the input label to the root node. 
      # use inversion formula to calculate the val of curr location in a normally ordered tree
          # inversion formula: (max number of current level + min number of current level) - current number
          # (max - curr) + min i.e find the node from min that is the same distance as curr from max.
          # For example to find the inversion of 14: 15 + 8 - 14 = 9
      # From here you just divide 9 by 2 to find the parent 4
# 3) You have to run the inversion formula at every level because at every level the row is inverted relative to the previous row

##########################################################################################################
# TC: O(3 * log n)
# SC: O(log n)

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [] # O(log n) space
        
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count*2: # O(log n) time
            node_count *= 2
            level += 1
            
        # Iterate from the target label to the root
        while label != 0: # O(log n) time
            res.append(label)
            level_max = 2**(level) - 1
            level_min = 2**(level - 1)
            label = int((level_max + level_min - label)/2)
            level -= 1
            
        return res[::-1] # O(n) time
        
