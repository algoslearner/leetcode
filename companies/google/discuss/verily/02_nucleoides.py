# https://leetcode.com/discuss/interview-question/1122743/Verily-Interview-Question
'''
// DNA is a long molecule that consists of a string of units called nucleotides. There are 4 types
// of nucleotides, represented by the letters "A", "T", "C", and "G". Given two inputs: an arbitrary
// DNA sequence and a list of DNA fragments, return true if the sequence can be constructed
// using some combination of the fragments, false otherwise.

// Examples:

// Input: "GTCAGAG", ["GTC", "AG"]
// Returns: True

// Input: "GTCAGAG", ["GTCA", "AGAG"]
// Returns: False
'''

# This is similar to Leetcode 139 : https://leetcode.com/problems/word-break/

def sequenceConstruction (word, tiles):
  # Check for base cases here

  lettersMatched = 0
  expectedMatches = len(word)
  currSubstring = ""

  for char in word:
    currSubstring += char
    if currSubstring in tiles:
      word = word[len(currSubstring):]
      lettersMatched += len(currSubstring)
      currSubstring = ""

  return lettersMatched == expectedMatches

print (sequenceConstruction("GTCAGAG", ["GTC", "AG"]))      # True
print (sequenceConstruction("GTCAGAG", ["GTCA", "AGAG"]))   # False
