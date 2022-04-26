# https://leetcode.com/discuss/interview-question/1474282/Amazon-OA
'''
'''

def simpleCipher(encrypted, k):
    k %= 26
    result = ""
    for char in encrypted:
        value = ord(char) - ord('A') - k
        if value < 0:
            value += 26
        value += ord('A')
        result += chr(value)
    return result

"""
Update 1: Adding an explanation on demand.
The string is made up of uppercase English letters only. That means a total of 26 characters, so if k is > 26 we have to adjust it back to 0..25 by doing modulo.
Now for each character, I am converting into ASCII and subtracting ASCII of 'A' as 'A' is our base value and then subtracting k to go k steps backward.
If the value is < 0 e.g k = 2 and the character is 'A' so the value will be -2, but what we want is a value between 0..25, so adding 26 into the value.
value is between 0..25 and 0 is mapped to 'A', 1 is mapped to 'B', and so on. So, basically, we have to add ASCII of 'A' again into the value.
Now just convert the ASCII to the character and append it to string.
"""

# question screenshot: https://cybergeeksquad.co/2022/02/simple-cipher-amazon-oa-solution.html
