# https://leetcode.com/problems/concatenated-words/
'''
Given a string and a list of words, find all the starting indices of substrings in the given string 
that are a concatenation of all the given words exactly once without any overlapping of words. 

It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
'''

##############################################################################################################
# sliding window + hashmaps
# TC: O(N * M * len)
# SC: O(N + M)


def find_word_concatenation(str1: string, words: List[str]) -> List[int]:
  if len(words) == 0 or len(words[0]) == 0:
    return []
  
  # load words into hashmap
  freqmap = {}
  for word in words:
    freqmap[word] = freqmap.get(word, 0) + 1
  
  output = []
  words_count = len(words)
  word_length = len(words[0])

  for i in range((len(str1) - words_count * word_length)+1):
    words_seen = {}
    for j in range(0, words_count):
      next_word_index = i + j * word_length
      # Get the next word from the string
      word = str1[next_word_index: next_word_index + word_length]
      if word not in freqmap:  # Break if we don't need this word
        break

      # Add the word to the 'words_seen' map
      if word not in words_seen:
        words_seen[word] = 0
      words_seen[word] += 1

      # No need to process further if the word has higher frequency than required
      if words_seen[word] > freqmap.get(word, 0):
        break

      if j + 1 == words_count:  # Store index if we have found all the words
        output.append(i)

  return output
                                
  
