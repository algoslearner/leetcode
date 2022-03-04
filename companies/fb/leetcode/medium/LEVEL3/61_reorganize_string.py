'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freqmap = {}
        for c in s:
            freqmap[c] = freqmap.get(c,0) + 1
        
        # insert all characters into a maxheap
        maxheap = []
        for char, freq in freqmap.items():
            heapq.heappush(maxheap,(-freq,char))
            
        # build string
        output = []
        previouschar = None
        previousfreq = 0
        while maxheap:
            freq, char = heapq.heappop(maxheap)
            if previouschar and -previousfreq > 0:
                heapq.heappush(maxheap, (previousfreq,previouschar))
            output.append(char)
            previouschar = char
            previousfreq = freq + 1 #decrement the negative number
        
        if len(output) == len(s):
            return "".join(output)
        else:
            return ""
            
        
