'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

######################################################################################
# READ: https://leetcode.com/problems/word-search-ii/solution/

# TC: O(M (4⋅3^L−1 )), where M is the number of cells in the board and LL is the maximum length of words.
# SC: O(N), , where NN is the total number of letters in the dictionary.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = True

        result = []
        def backtrack(i: int, j: int, node = trie, prefix: str = ''):
            letter = board[i][j]
            if letter in node:
                board[i][j] = '#'
                node = node[letter]
                if '$' in node:
                    result.append(prefix + letter)
                    del node['$']
                for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= r < rows and 0 <= c < cols:
                        backtrack(r, c, node, prefix + letter)
                board[i][j] = letter

        for i in range(rows):
            for j in range(cols):
                backtrack(i, j)
        
        return result
