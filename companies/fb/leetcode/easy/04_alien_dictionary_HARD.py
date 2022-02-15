'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
'''
# https://leetcode.com/problems/alien-dictionary/discuss/1564871/Python3-or-Topological-Sort-or-99.95-faster

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # build adj list
        adjacency_list = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        
        for first_word, second_word in zip(words, words[1:]):
            index = 0
            for ch1, ch2 in zip(first_word, second_word):
                index += 1
                if ch1 != ch2:
                    adjacency_list[ch1].append(ch2)
                    in_degree[ch2] += 1
                    break # only first different character matters
                # when input is ["abc","ab"] this should return ""
                if index == min(len(first_word), len(second_word)) and len(first_word) > len(second_word):
                    return ""
        
        
        # check no of unique characters
        characters = set()
        for word in words:
            for ch in word:
                characters.add(ch)
        
        if len(characters) == 1:
            return characters.pop()
        
        # add characters with 0 in-degree to stack
        stack = []
        for ch in characters:
            if ch not in in_degree:
                stack.append(ch)
        
        # topological sort
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            
            for neighbor in adjacency_list[node]:
                if in_degree[neighbor] > 1:
                    in_degree[neighbor] -= 1
                elif in_degree[neighbor] == 1:
                    stack.append(neighbor)
                    
        return "".join(res) if len(res) == len(characters) else ""
        # if true: topological sort is possible and di-graph is acyclic
        # else: di-graph is cyclic
        
