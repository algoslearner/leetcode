#
'''
Structurally Unique Binary Search Trees (hard) #
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

Example 1:

Input: 2
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:

Example 2:

Input: 3
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1 to 3: 
'''

###################################################################################################################################
# subsets
# TC: exponential: O(n * 2^n)
# SC: O(2^n)


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_unique_trees(n):
  if n <= 0:
    return []
  return findUnique_trees_recursive(1, n)


def findUnique_trees_recursive(start, end):
  result = []
  # base condition, return 'None' for an empty sub-tree
  # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
  # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
  # both of these should return 'None' for the left and the right child
  if start > end:
    result.append(None)
    return result

  for i in range(start, end+1):
    # making 'i' the root of the tree
    leftSubtrees = findUnique_trees_recursive(start, i - 1)
    rightSubtrees = findUnique_trees_recursive(i + 1, end)
    for leftTree in leftSubtrees:
      for rightTree in rightSubtrees:
        root = TreeNode(i)
        root.left = leftTree
        root.right = rightTree
        result.append(root)

  return result


def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()

'''
Output
0.71s
Total trees: 2
Total trees: 5
'''
