'''
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

 

Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
 

Constraints:

1 <= s.length <= 16
s consists of only lowercase English letters.
'''

# READ: related backtracking problems and solutions
# https://leetcode.com/problems/palindrome-permutation-ii/discuss/69717/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)


# https://leetcode.com/problems/palindrome-permutation-ii/discuss/1403853/Python-backtracking%3A-build-string-from-the-middle

'''
If you have some familiarity with palindromes, you should know that a palindrome can only be constructed from a set of letters if and only if at most one character has an odd count. If so, this odd-count character will be in the middle of the string.

We can construct palindromes by considering two scenarios, either there is one character that has an odd count, or all characters have even counts.

If all characters have even counts, the process of backtracking is simple. For each remaining character, we simply add it to each side of the current solution. One branch of the backtracking solution would grow like this:

initial counter: {'a' : 2, 'b' : 2, 'c' : 2}

cur: '', remaining: {'a' : 2, 'b' : 2, 'c' : 2}
cur: 'aa', remaining: {'b' : 2, 'c' : 2}
cur: 'baab', remaining: {'c' : 2}
cur: 'cbaabc', remaining: {} # no more characters, add cur to result and backtrack

If one character has an odd count, we start with the odd-count character as cur and repeat the same process. It would look something like this:

initial counter: {'a' : 2, 'b' : 2, 'c' : 2, 'i' : 1}

cur: 'i', remaining: {'a' : 2, 'b' : 2, 'c' : 2}
cur: 'aia', remaining: {'b' : 2, 'c' : 2}
cur: 'baiab', remaining: {'c' : 2}
cur: 'cbaiabc', remaining: {} # no more characters, add cur to result and backtrack

Once you've made this observation this should be a standard backtracking problem.
'''

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        res = []
        
        def backtrack(cur=""):
            if not counter:
                res.append(cur)
                return
            for c in list(counter.keys()):
                counter[c] -= 2
                if not counter[c]:
                    del counter[c]
                backtrack(c+cur+c)
                counter[c] += 2

        oddCounts = [c for c in counter if counter[c]%2] # The characters in counter with odd count
        
        if not len(oddCounts): # if no odd chars, we can simply backtrack
            backtrack()
            
        if len(oddCounts) == 1: # if exactly one odd char, backtrack with oddChar in the middle of string
            oddChar = oddCounts[0]
            counter[oddChar] -= 1
            if not counter[oddChar]:
                del counter[oddChar]
            backtrack(oddChar)
            
        return res
