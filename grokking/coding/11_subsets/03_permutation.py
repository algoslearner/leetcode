#
'''
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!
n!
 permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

##############################################################################################################################################
# subsets - iterative
# TC: O(N * N!)
# SC: O(N * N!)

from collections import deque

def find_permutations(nums):
  output = []
  dq = deque()
  dq.append([])

  for curr in nums:
    for _ in range(len(dq)):
      oldperm = dq.popleft()
      for j in range(len(oldperm) + 1):
        newperm = list(oldperm)
        newperm.insert(j, curr)
        if len(newperm) == len(nums):
          output.append(newperm)
        else:
          dq.append(newperm)

  return output


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

'''
Output
1.05s
Here are all the permutations: [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]
'''

##############################################################################################################################################
# recursion
# TC: O(N * N!)
# SC: O(N * N!)

def generate_permutations(nums):
  result = []
  generate_permutations_recursive(nums, 0, [], result)
  return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
  if index == len(nums):
    result.append(currentPermutation)
  else:
    # create a new permutation by adding the current number at every position
    for i in range(len(currentPermutation)+1):
      newPermutation = list(currentPermutation)
      newPermutation.insert(i, nums[index])
      generate_permutations_recursive(
        nums, index + 1, newPermutation, result)


def main():
  print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))


main()

