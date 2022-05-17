# https://leetcode.com/problems/create-binary-tree-from-descriptions/
'''
2196. Create Binary Tree From Descriptions

Share
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 

Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
'''

####################################################################################################
# HASHMAP
# https://leetcode.com/problems/create-binary-tree-from-descriptions/discuss/1823678/Python-Solution-using-HashMap-with-Steps
# TC: O(N)
# SC: O(N)

# STEPS
'''
Here we use a HashMap to keep track of node values and their references along with the fact if that node has a parent or not. We develop the Binary Tree as we go along. Finally we check which node has no parent as that node is the root node.

Maintain a hash map with the keys being node values and value being a list of its REFERENCE and a HAS_PARENT property which tells weather or not it has a parent or not (Represented by True if it has False if not)
Traverse through the descriptions list.
For every new node value found, add a new TreeNode into the list with its HAS_PARENT property being False.
Now make the child node parents left/right child and update the HAS_PARENT property of child value in map to True.
Now once the Binary Tree is made we traverse through the hash map to check which node still has no parent. This node is out root node.
Return the root node.
'''

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = None
        table = {}
        for arr in descriptions:
            parent = arr[0]
            child = arr[1]
            isleft = arr[2]
            if table.get(parent, None) is None: # If key parent does not exist in table
                table[parent] = [TreeNode(parent), False]
            if table.get(child, None) is None: # If key child does not exist in table
                table[child] = [TreeNode(child), False]
            table[child][1] = True # Since child is going to have a parent in the current iteration, set its has parent property to True
            if isleft == 1:
                table[parent][0].left = table[child][0]
            else:
                table[parent][0].right = table[child][0]
		# Now traverse the hashtable and check which node still has no parent
        for k, v in table.items():
            if not v[1]: # Has parent is False, so root is found.
                root = k
                break
        return table[root][0]


############################################################################
# SET
# https://leetcode.com/problems/create-binary-tree-from-descriptions/discuss/1823804/Python-Solution
'''
Explanation
Iterate descriptions,
for each [p, c, l] of [parent, child, isLeft]

Create Treenode with value p and c,
and store them in a hash map with the value as key,
so that we can access the TreeNode easily.

Based on the value isLeft,
we assign Treenode(parent).left = Treenode(child)
or Treenode(parent).right = Treenode(child).

Finally we find the root of the tree, and return its TreeNode.
'''

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        m = {}
        for p,c,l in descriptions:
            np = m.setdefault(p, TreeNode(p))
            nc = m.setdefault(c, TreeNode(c))
            if l:
                np.left = nc
            else:
                np.right = nc
            children.add(c)
        root = (set(m) - set(children)).pop()
        return m[root]
