'''
Given a word, find out how many times you'd need the word "facebook" to spell it out.
'''
import collections

def countLabels(word):
  
  # word freq count
  wordfreq = collections.Counter(word)
  fbfreq = collections.Counter("facebook")
  
  count = 1
  for c in wordfreq.keys():
    if c not in fbfreq:
      print("Error: given word has extra alphabets")
      return -1
    elif wordfreq[c] > count * fbfreq[c]: count += 1
  print(count)
  
#########################################################################################  
# TESTS
# word = "face"
# word = "facef"
# word = "foooce"
word = "price"
countLabels(word)

# output: word = "face"
'''
1
'''
# output: word = "foooce"
'''
2
'''
#output : word = "price"
'''
Error: given word has extra alphabets
'''
