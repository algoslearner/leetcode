#
'''
Problem Statement#
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

###############################################################################################################################
# SLIDING WINDOW
# TC: O(N)
# SC: O(1)

def fruits_into_baskets(fruits):
  max_length = 0
  start = 0
  freqmap = {}
  
  for end in range(len(fruits)):
    right_fruit = fruits[end]
    if right_fruit in freqmap:
      freqmap[right_fruit] += 1
    else:
      freqmap[right_fruit] = 1
  
    # shrink the sliding window
    while len(freqmap) > 2:
      left_fruit = fruits[start]
      freqmap[left_fruit] -= 1
      if freqmap[left_fruit] == 0: del freqmap[left_fruit]
      start += 1
  
    max_length = max(max_length, end - start + 1)
  return max_length
  
