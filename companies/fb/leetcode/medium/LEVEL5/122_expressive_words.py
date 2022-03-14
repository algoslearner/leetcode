'''
Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

 

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3
 

Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
'''

################################################################
'''
Loop through all words. check(string S, string W) checks if W is stretchy to S.

In check function, use two pointer:

If S[i] == W[j, i++, j++
If S[i - 2] == S[i - 1] == S[i] or S[i - 1] == S[i] == S[i + 1], i++
return false
'''

class Solution:
    def expressiveWords(self, S, words):
        return sum(self.check(S, W) for W in words)

    def check(self, S, W):
        i, j, n, m = 0, 0, len(S), len(W)
        for i in range(n):
            if j < m and S[i] == W[j]: j += 1
            elif S[i - 1:i + 2] != S[i] * 3 != S[i - 2:i + 1]: return False
        return j == m
        
