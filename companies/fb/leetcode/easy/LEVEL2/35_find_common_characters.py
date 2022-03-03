'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''

# https://leetcode.com/problems/find-common-characters/discuss/473485/Python-99.60-Short-and-Understandable-Solution
'''
Idea is simple:

We loop over the unique characters in the first word because for a letter to be considered it must be in all words including first word.

Comparing each character in first word with all other words.

Check if the character in comparison in the first world exists in the word in comparison

If it does then count its count and compare with existing count and take the min. Also increment the occurences to see if this character exists in all words.

If it doesn't then break from the loop as now one of characters isn't in first words and we are no longer interested in it.

After inside loop exits, check if occurences amount equals that of the amount of words we have to make sure the character in question exists in all the words.

Lastly add this character which exists in all words with its minimum occurence.
'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        word1 = set(words[0])
        for c in word1:
            count = words[0].count(c)
            occurences = 1
            for i in range(1,len(words)):
                if c in words[i]:
                    count = min(count,words[i].count(c))
                    occurences += 1
                else:
                    break
            if occurences == len(words):
                for i in range(count):
                    result.append(c)
                    
        return result
