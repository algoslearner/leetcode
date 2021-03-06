'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
'''

###################################################
'''
Approach #1: Brute Force [Accepted]

Intuition:
For each word, check if all prefixes word[:k] are present. 
We can use a Set structure to check this quickly.

Algorithm:
Whenever our found word would be superior, we check if all it's prefixes are present, then replace our answer.
Alternatively, we could have sorted the words beforehand, so that we know the word we are considering would be the answer if all it's prefixes are present.
'''

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Brute Force: set and sort
        # TC: O(n2), SC: O(n2)
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""
       
       
###########################################
# Build Trie + DFS
'''
Intuition
As prefixes of strings are involved, this is usually a natural fit for a trie (a prefix tree.)

Algorithm
Put every word in a trie, then depth-first-search from the start of the trie, only searching nodes that ended a word. 
Every node found (except the root, which is a special case) then represents a word with all it's prefixes present. 
We take the best such word.

In Python, we showcase a method using defaultdict.
'''
# TC: O(sum(n))
# SC: O(sum(n))
class Solution:
    def longestWord(self, words: List[str]) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = list(trie.values())
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans
