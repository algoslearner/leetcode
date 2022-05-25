# https://leetcode.com/problems/repeated-dna-sequences/
'''
187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, 
return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
'''

#####################################################################################
# String slice + hashset
# TC: O(N), since length of sequence is 10
# SC: O(N), since Length of sequence is 10

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        n = len(s)
        output = set()
        seen = set()
        
        for start in range(n - L + 1):
            tmp = s[start: start + L]
            if tmp in seen:
                output.add(tmp)
            seen.add(tmp)
        
        return output

