#
'''
Count of Structurally Unique Binary Search Trees (hard)#
Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

Example 1:

Input: 2
Output: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.
Example 2:

Input: 3
Output: 5
Explanation: There will be 5 unique BSTs that can store numbers from 1 to 3.
'''

################################################################################################################################################
# recursion
# tc: O(2^n)
# sc: O(2^n)


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  if n <= 1:
    return 1
  count = 0
  for i in range(1, n+1):
    # making 'i' root of the tree
    countOfLeftSubtrees = count_trees(i - 1)
    countOfRightSubtrees = count_trees(n - i)
    count += (countOfLeftSubtrees * countOfRightSubtrees)

  return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()

'''
Output
1.12s
Total trees: 2
Total trees: 5
'''


################################################################################################################################################
# recursion + memoization
# tc: O(n^2)
# sc: O(n)

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  return count_trees_rec({}, n)


def count_trees_rec(map, n):
  if n in map:
    return map[n]

  if n <= 1:
    return 1
  count = 0
  for i in range(1, n+1):
    # making 'i' the root of the tree
    countOfLeftSubtrees = count_trees_rec(map, i - 1)
    countOfRightSubtrees = count_trees_rec(map, n - i)
    count += (countOfLeftSubtrees * countOfRightSubtrees)

  map[n] = count
  return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()
