#
'''
There is a dictionary containing words from an alien language for which we don’t know the ordering of the letters.
Write a method to find the correct order of the letters in the alien language. 
It is given that the input is a valid dictionary and there exists an ordering among its letters.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
from the given words we can conclude the following ordering among its characters:

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

From the above two points, we can conclude that the correct character order is: "bac"
Example 2:

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

From the above two points, we can conclude that the correct character order is: "cab"
Example 3:

Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among its characters:

1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

From the above five points, we can conclude that the correct character order is: "ywxz"
'''

#####################################################################################################################
# TC: O(V + N)
# SC: O(V + N)

from collections import deque

def find_order(words):
  sortedOrder = []
  
  if len(words) == 0:
    return ""

  # initialize graph
  indegree = {}
  adj_list_graph = {}
  for word in words:
    for c in word:
      indegree[c] = 0
      adj_list_graph[c] = []
  
  # build graph
  for i in range(0, len(words) - 1):
    w1, w2 = words[i], words[i + 1]
    for j in range(0, min(len(w1), len(w2))):
      parent, child = w1[j], w2[j]
      if parent != child:
        adj_list_graph[parent].append(child)
        indegree[child] += 1
        break # only the first different character, helps to find order
  
  # find all sources
  sources = deque()
  for key in indegree:
    if indegree[key] == 0:
      sources.append(key)
  
  # for each source, populate sortedOrder
  while sources:
    source = sources.popleft()
    sortedOrder.append(source)
    for child in adj_list_graph[source]:
      indegree[child] -= 1
      if indegree[child] == 0: sources.append(child)
  
  # if any cycle
  if len(sortedOrder) != len(indegree):
    return ""

  # order
  return ''.join(sortedOrder)

def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()


