#
'''
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''

##########################################################################################################################################################################
# subset
# TC: O(N * 2^N)
# SC: O(N * 2^N)

def find_letter_case_string_permutations(word):
  output = []
  output.append(word)

  for i in range(len(word)):
    if word[i].isalpha():
      for j in range(len(output)):
        curr_chars = list(output[j])
        curr_chars[i] = curr_chars[i].swapcase()
        output.append(''.join(curr_chars))
  
  return output


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()

'''
Output
0.8s
String permutations are: ['ad52', 'Ad52', 'aD52', 'AD52']
String permutations are: ['ab7c', 'Ab7c', 'aB7c', 'AB7c', 'ab7C', 'Ab7C', 'aB7C', 'AB7C']
'''
