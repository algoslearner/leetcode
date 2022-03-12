'''
You are given an array of strings of the same length words.

In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].

For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
A group of special-equivalent strings from words is a non-empty subset of words such that:

Every pair of strings in the group are special equivalent, and
The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
Return the number of groups of special-equivalent strings from words.

 

Example 1:

Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: 
One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these.
The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
Note that in particular, "zzxy" is not special equivalent to "zzyx".
Example 2:

Input: words = ["abc","acb","bac","bca","cab","cba"]
Output: 3
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 20
words[i] consist of lowercase English letters.
All the strings are of the same length.
'''

###########################################################################################
# https://leetcode.com/problems/groups-of-special-equivalent-strings/discuss/358795/python3-detail-explanation-of-special-equivalent
'''
The point here is to understand the following requirement:
A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].
Don't trap your thoughts by the word 'swap'.
Your goal is how to identify the equivalent strings.

There are two possible outcomes of i%2: 1 or 0. i is the index of the input string.
if i % 2 ==1: i = 1,3,5,7 ... in other words, i is odd number. In other words, the order of the odd index's value doesn't matter here. You can swap them.
if i % 2 ==0: i = 0,2,4,6 ... in other words, i is even number. In other words, the order of the even index's value doesn't matter here. You can swap them.

So sort the string's odd index elements, and sort the string's even index elements and combine them to create a new string called "sort_string."
If two string has the same "sort_string," they are the special-equivalent strings.

A = ["abcd","cdab","adcb","cbad"]
      ### sort odd index element      | sort even index element
"abcd" :              bd              |               ac
"cbad" :              bd              |               ac
"adcb" :              bd              |               ac
"cdab" :              bd              |               ac
# so they are equivalent strings
'''

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        res = set()
        for s in words:
            sort_odd_even = ''.join(sorted(s[1::2]) + sorted(s[::2]))
            res.add(sort_odd_even)
        return len(res)
