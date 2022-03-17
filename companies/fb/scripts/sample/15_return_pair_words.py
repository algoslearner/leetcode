#
'''
Given a set of words return a pair with prefix and then the full word. The words will only contain english lower case letters and input words are not sorted. Return the pair of words with the small word and then the larger word, for ex - 'be' then 'bee'.

Input : ["abs","app","be","apple","bee","better","bet","absolute"]
Output: [("abs","absolute"),("app","apple"),("be","bee"),("bet","better")]

I couldn't solve the problem on time however, it seems to be a trie problem where all the input words can be put in the trie and scan again. Any pointers or thoughts on how to solve?

Update: updated example with format with few more strings
'''

# Trie is way too complicated for this. "Prefix" doesn't always mean "Trie"

def return_pairs(words_array):
    pairs = []
    last_prefix = None
    # O(nlogn + n)
    for word in sorted(words_array):
        if last_prefix and word.startswith(last_prefix):
            pairs[-1].append(word)
        else:
            last_prefix = word
            pairs.append([word])
    return pairs

  # Keep in mind that phone screen questions should be doable in 20-30 mins.
  '''
Input : ["apple", "be", "app", "bee", "bet", "better", "abs", "absolute"]
Sorted : ['abs', 'absolute', 'app', 'apple', 'be', 'bee', 'bet', 'better'] (print from above code)

Actual : [['abs', 'absolute'], ['app', 'apple'], ['be', 'bee', 'bet', 'better']]
Expected : [['abs', 'absolute'], ['app', 'apple'], ['be', 'bee',], ['bet', 'better']]
  '''
