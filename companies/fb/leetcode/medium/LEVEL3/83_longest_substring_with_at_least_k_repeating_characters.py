'''
Given a string s and an integer k, 
return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # brute force
        # TC : O(n)
        # SC: O(n)
        for char, count in Counter(s).items():
            if count < k:
                return max(self.longestSubstring(s, k) for s in s.split(char))
        return len(s)

'''
The key is to check the characters that do not satisfy the condition

Taking out those characters out with split
And check all the "substrings" one by one
Beautiful move!
'''

# TC : O(n), since alphabets set is 26
# SC: O(n)
# recursive
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)

# iterative
class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        stack = []
        stack.append(s)
        ans = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])
                    break
            else:
                ans = max(ans, len(s))
        return ans
