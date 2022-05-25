# https://leetcode.com/problems/shortest-word-distance-ii/
'''
244. Shortest Word Distance II

Design a data structure that will be initialized with a string array, 
and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:
WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 

Example 1:

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
 

Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
'''

####################################################################################################
# two pointers
# TC: O(N)
# SC: O(1)

# difference from shortest word distance 1
'''
One difference is here you are asked to create a data structure with shortest method. 
This method will be called multiple times. 
So if you use the soln of word distance 1, it will go through entire list every time, which will be bad. 
Thus you need to precompute the indices in map of { word -> list of indices } structure. 
so that when method is called, you are only comparing two lists which are much shorter than entire list of all words. 
Hope that helps.
'''

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]
        
        # until shorter of two lists are processed
        shortest = float('inf')
        i = j = 0
        while i < len(loc1) and j < len(loc2):
            shortest = min(shortest, abs(loc1[i] - loc2[j]))
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1
        return shortest
            
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
