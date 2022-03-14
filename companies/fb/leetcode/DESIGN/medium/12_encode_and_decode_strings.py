'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
 

Follow up: Could you write a generalized algorithm to work on any possible set of characters?
'''

########################################################################################################
'''
Approach 1: Non-ASCII Delimiter
Intuition

Naive solution here is to join strings using delimiters.

What to use as a delimiter? Each string may contain any possible characters out of 256 valid ascii characters.

Seems like one has to use non-ASCII unichar character, for example unichr(257) in Python and Character.toString((char)257) in Java (it's character ā).

fig

Here it's convenient to use two different non-ASCII characters, to distinguish between situations of "empty array" and of "array of empty strings".

Implementation

Use split in Java with a second argument -1 to make it work as split in Python.
'''

class Codec:
    def encode(self, strs: [str]) -> str:
        msg =  ''
        for s in strs : 
            msg+=s + chr(259)
        msg=msg[0:len(msg)-1]   
        return msg     
        
    def decode(self, s: str) -> [str]:
        lst = s.split(chr(259)) 
        return lst 
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
