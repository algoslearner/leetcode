'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''

# https://leetcode.com/problems/string-to-integer-atoi/discuss/748024/Python3-solution-with-a-Process-for-coding-interviews
'''
Hello,

Here is my solution with a process to follow during a coding interview:

Problem Summary / Clarifications / TDD:
- Q1. What if there is a space between the sign and the number? (see cases 5 and 6)
- Q2. What if the result is not an int. Python manages overflow issues. See case 12 and 14.

Case.01. myAtoi("           ") = 0          (a non valid number with spaces only)
Case.02. myAtoi("words      ") = 0          (a non valid number only)
Case.03. myAtoi("words12365 ") = 0          (a non valid number is followed by a valid number I)
Case.04. myAtoi("words 1236 ") = 0          (a non valid number is followed by a valid number II)
Case.05. myAtoi("+ 4193"     ) = 0          (a non valid number: space between sign and number I)
Case.06. myAtoi("- 4193    " ) = 0          (a non valid number: space between sign and number II)

Case.07. myAtoi("4193"       ) = 4193       (a valid number only)
Case.08. myAtoi("4193word"   ) = 4193       (a valid number is followed by a non valid number I)
Case.09. myAtoi("4193 word"  ) = 4193       (a valid number is followed by a non valid number II)
Case.10. myAtoi("4193 12 wo" ) = 4193       (a valid number is followed by a another valid number)
Case.11. myAtoi("+4193"      ) = 4193       (a positive valid number with the sign +)
Case.12. myAtoi("+2147483648") = 2147483647 (a positive number greater than int max value)
Case.13. myAtoi("-4193"      ) = -4193      (a negatve valid number with the sign -)
Case.14. myAtoi("-2147483649") = -2147483648(a negative number less than int min value)
Intuition:
1. Extract the number (str_num) from s
2. Extract the sign from str_num
3. Loop each digit of str_num and compute the conversion in num
4. Break when a non digit char is found or num reach max/min int
5. Return num * sign

Implementation: see below

Tests: Use all tests created in step 1 (TDD)

Analysis:

Time Complexity: O(|s|)
Space Complexity: O(|s|)
Could we do better?
Time Complexity: We can't in term of asymptotique analysis but if we don't use the split function and break as soon as a non valid digit is found, the code may be faster
Space Complexity: Yes, we could make it O(1) if we don't use the split function and we loop on each character of s
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        str_list = s.split()
        
        if not str_list:
            return 0
                
        num_str = str_list[0]
        sign = -1 if num_str[0] == '-' else +1
        start = 1 if num_str[0] in '-+' else 0
        
        num = 0
        int_boundary =  0x80000000 if sign == -1 else 0x7fffffff # 2147483648 or 2147483647
        
        for i in range(start, len(num_str)):
            ord_digit = ord(num_str[i])
            if ord_digit < 48 or ord_digit > 57:
                break
            
            num *= 10
            num += ord_digit - 48
            
            if num >= int_boundary:
                num = int_boundary
                break
        
        return num * sign
