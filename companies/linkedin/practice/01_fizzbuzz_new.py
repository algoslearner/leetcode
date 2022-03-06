'''
Write a program which prints out all numbers between 1 and 100. 
When the program would print out a number exactly divisible by 4, print "Linked" instead. 
When it would print out a number exactly divisible by 6, print "In" instead. When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn."
'''

class Solution:
  def printLinkedin():
    output = []
    for i in range(1,101):
      if i % 4 == 0 and i % 6 == 0:
        output.append("LinkedIn")
      elif i % 4 == 0:
        output.append("Linked")
      elif i % 6 == 0:
        output.append("In")
      else:
        output.append(str(i))
    print(output)
