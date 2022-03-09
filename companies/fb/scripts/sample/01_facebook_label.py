'''
Given a word, find out how many times you'd need the word "facebook" to spell it out.
'''

def countLabels(word: str) -> int:
  
  if set(word) != set("facebook"):
    return -1
  
  # word freq count
  wordfreq = collections.Counter(word)
  fbfreq = collections.Counter("facebook")
  
  count = 1
  for c in freq:
    if wordfreq[c] > count * fbfreq[c]:
      count += 1
  return count
