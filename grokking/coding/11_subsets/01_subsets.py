#
'''
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''

##############################################################################################################################
# TC: O(N * 2^N)
# SC: O(N * 2^N)

def find_subsets(nums):
  output = []
  output.append([])

  for curr in nums:
    for i in range(len(output)):
      set1 = list(output[i])
      set1.append(curr)
      output.append(set1)


  return output
