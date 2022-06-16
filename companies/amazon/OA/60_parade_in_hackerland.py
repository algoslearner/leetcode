# https://leetcode.com/discuss/interview-question/2131732/Amazon-OA
'''
Parade in HackerLand
The people in HackerLand, are getting ready for a parade, and the participants are all mixed up. There should be no instance where a red uniform is immediately to the left of a blue one.
Given a binary string, 0 denotes a person in red uniform and 1 denotes a person in blue uniform. The goal is to remove any occurrence of "01" in the binary string. More formally, at each second, all the substrings "01 "in the string s are changed to "10". This process repeats until no "0/11 is present in the string. All the substrings "01" in the current state of sare changed at the same time.
Find the number of seconds it takes for this process to stop.
Example color = "001011"
Here is a simulation of the process where t denotes the current time. t= 0, color = "001011" t= 1, color = "010101" t= 2, color = "101010" t= 3, color = "110100" t= 4, color = "111000"
0101->1010->1100 ans:2

Hence this process takes 4 seconds.

int getSwapTime(String color){
}
'''
