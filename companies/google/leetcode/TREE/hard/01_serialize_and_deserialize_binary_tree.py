'''
Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                output.append("None,")
                return
            output.append(str(root.val) + ",")
            dfs(root.left)
            dfs(root.right)
            
        output = []
        dfs(root)
        return "".join(output)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def helper(data_list):
            if data_list[0] == "None":
                data_list.pop(0)
                return None
            
            root = TreeNode(data_list[0])
            data_list.pop(0)
            root.left = helper(data_list)
            root.right = helper(data_list)
            return root
        
        data_list = data.split(",")
        root = helper(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

#################################################################
# TC: O(N), in both serialization and deserialization functions, we visit each node exactly once, thus the time complexity is O(N), where NN is the number of nodes, i.e. the size of tree.
# SC: O(N), in both serialization and deserialization functions, we keep the entire tree, either at the beginning or at the end, therefore, the space complexity is O(N).
