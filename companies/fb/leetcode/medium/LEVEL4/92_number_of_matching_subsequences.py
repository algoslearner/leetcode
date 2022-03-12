'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
'''

# https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation
'''
Hello! Before I explain my solution, I would like to give credit to the post that inspired it. Here is a link with a description of the original algorithm.

I begin by creating a default dictionary of 'list' objects. 
The main benefit of a default dictionary is that when you access an entry that does not yet exist, 
the entry is created automatically (in this case, the value for the entry is an empty list when it is created). 
I then create a 'count' variable to keep track of the number of words that are subsequences of the given string.

The first thing I do with the dictionary is populate it with all the words in the list of words. 
The key for each entry is the first letter of the word. 
The value is the list of words that start with that letter. 

Using the example in the problem, the dictionary would look like the following:
{'a': ['a', 'acd', 'ace'], 'b': ['bb']}

The next step is to iterate through each character in the given string.
For each character, I access the dictionary to retrieve the list of words that start with that character. 
I reset the value of the entry to an empty list and then iterate through the list of words I retrieved. 
If the word is only a single letter, then I conclude that we have successfully found a completed subsequence and increase our 'count' by one. 
Otherwise, I slice off the first character and add the sliced word back to the dictionary. 
This time, it is added to the entry for which the key is equal to the first letter of the sliced word.

This process continues until we have iterated through all characters in the string. 
At the end, I return the count.
'''

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        
        word_dict = defaultdict(list)
        for word in words:
            word_dict[word[0]].append(word)            
        
        for c in s:
            words_expecting_char = word_dict[c]
            word_dict[c] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
