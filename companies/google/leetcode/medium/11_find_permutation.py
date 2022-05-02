# https://leetcode.com/problems/find-permutation/
'''
484. Find Permutation

A permutation perm of n integers of all the integers in the range [1, n] can be represented as a string s of length n - 1 where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the lexicographically smallest permutation perm and return it.

 

Example 1:

Input: s = "I"
Output: [1,2]
Explanation: [1,2] is the only legal permutation that can represented by s, where the number 1 and 2 construct an increasing relationship.
Example 2:

Input: s = "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can be represented as "DI", but since we want to find the smallest lexicographical permutation, you should return [2,1,3]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
'''

#####################################################################################################
# STACK
# TC: O(n)
# SC: O(n)
        ## LOGIC ##
        ## 1. When we get D, we push and when we get I, we calculate previous maximum value and calculate the next number i.e prev + 1 and add to current I position and as only D's are in the stack and they have lower precedence than I, we pop all incrementing the prev value updated
        ## 2. To simplify the things, I have appended I at the end. ( if there are any D's left in the stack, this will take care and also we are missing out the last number, i.e len(s), so include that aswell we need I at the end)

        ## EXAMPLE : "DDIIDDID"	##
		## STACK TRACE ##
        # D [0, 0, 0, 0, 0, 0, 0, 0, 0] [('D', 0)]
        # D [0, 0, 0, 0, 0, 0, 0, 0, 0] [('D', 0), ('D', 1)]
        # I [3, 2, 1, 0, 0, 0, 0, 0, 0] []
        # I [3, 2, 1, 4, 0, 0, 0, 0, 0] []
        # D [3, 2, 1, 4, 0, 0, 0, 0, 0] [('D', 4)]
        # D [3, 2, 1, 4, 0, 0, 0, 0, 0] [('D', 4), ('D', 5)]
        # I [3, 2, 1, 4, 7, 6, 5, 0, 0] []
        # D [3, 2, 1, 4, 7, 6, 5, 0, 0] [('D', 7)]
        # I [3, 2, 1, 4, 7, 6, 5, 9, 8] []

class Solution:
    def findPermutation(self, s: str) -> List[int]:        
        stack = []
        # indicates the value of the last element that is put in the ans array
        prev = 0
        ans = [0] *(len(s)+1)
        for i, ch in enumerate(s + "I"):
            if( ch == "I" ):
                prev = prev + 1
                ans[i] = prev
                while( stack ):
                    prev += 1
                    ans[stack.pop()] = prev
            else:
                stack.append(i)
            # print(ch, ans, stack)
        return ans

#####################################################################################################
# reverse
# TC: 
# SC: 
# Reversing the subarray: we first fill all the answer array with 1 to n sequentially, 
# then from the first occurance of D to first occurance of I, we reverse all values including the Dth and Ith position.

#####################################################################################################
# two pointers
# TC: O(n)
# SC: O(1)
# https://leetcode.com/problems/find-permutation/discuss/1999094/Python-Two-pointers-Easy-understanding-for-Beginners

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n,perm=len(s),[]
        for i in range(1,len(s)+2):
            perm.append(i)
        
        left,right=0,0
        while left<n:
            if s[right]=='D':
                while right<n and s[right]=='D':
                    right+=1
                perm[left:right+1]=perm[left:right+1][::-1]
                left=right
            else:
                left+=1
                right+=1
        return perm
