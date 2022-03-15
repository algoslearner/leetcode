'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

##################################################################################################################################
# https://leetcode.com/problems/longest-palindromic-subsequence/discuss/1096936/PYTHON-DP-FOR-DUMMIES
'''
Problem: Longest palindromic substring.

Translation: We should look at all the substrings strategically. We need to use max somewhere (keyword: longest), plus we don't care when we don't have a palindrome bc we just need to keep track of the longest one so far.

Dynammic Programming: So.. of course we will be using DP bc there can be repeating calculations. Ex. bb -> bbbb -> bbbbbb only needs three calculations bc we can use what we've seen before to calculate the next valid palindrome. Aka if s[i+1:j-1] is a palindrome, then s[i:j] is a palindrome too if s[i] == s[j].

But how do we build this up? Since we know we need to keep track of indices i and j lets use a dp grid to keep track of all the combinations of i and j that we will look at.

s = "bbbab"
dp = 
    b b b a b
b[[ _ _ _ _ _ ] , 
b [ _ _ _ _ _ ], 
b [ _ _ _ _ _ ], 
a [ _ _ _ _ _ ], 
b [ _ _ _ _ _ ]] 
Each item in the grid will keep track of the longest palindrome thus far in s[i:j]. This means we can use our before formula to calculate each step in the grid based on our previous steps.

If the string is 1 character length, we have a palindrome of length 1.
If the string is 2 charaters length, and the characters are equal, then we have a palindrome of length 2.
Else if we find a new palindrome (building off a previous palindrome), we have lenNewPalindrome = len(previousPalindrome) + 2
Else we have no new palindromes, our longestPalindrome will be equal to the longest palindrome we have seen so far bc nothing has changed essentially.
So our final grid will look like this:

s = "bbbab"
dp = 
   b  b  b  a  b
b[[1, 2, 3, 3, 4],
b [0, 1, 2, 2, 3],
b [0, 0, 1, 1, 3],
a [0, 0, 0, 1, 1],
b [0, 0, 0, 0, 1]]
With every substring building off the previously calculated longestPalindrome.
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for k in range(1, len(s) + 1):
            for i in range(len(s) - k + 1):
                j = k + i - 1
                if i == j:
                    dp[i][j] = 1
                elif i + 1 == j and s[i] == s[j]:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
        
