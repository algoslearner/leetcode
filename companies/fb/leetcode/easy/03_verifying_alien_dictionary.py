'''
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
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
        
