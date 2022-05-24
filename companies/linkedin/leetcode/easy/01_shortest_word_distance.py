# https://leetcode.com/problems/shortest-word-distance/
'''
243. Shortest Word Distance

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
'''

############################################################################################################
# TC: O(N)
# SC: O(1)

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest = start = end = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                start = i
            elif wordsDict[i] == word2:
                end = i
            shortest = min(shortest, abs(start - end))
        return shortest
