'''
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 

Constraints:

0 <= num <= 231 - 1
'''

# TC: O(N)
# SC: O(1)

class Solution:
    def numberToWords(self, num: int) -> str:
        def helper(num):
            result=""
            belowTen=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
            belowTwenty=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
            belowHundred=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
            if(num<10):
                result= belowTen[num]
            elif(num>=10 and num<20):
                result= belowTwenty[num-10]
            elif  (num>=20 and num<100):
                result= belowHundred[int(num/10)-2] +" " +  helper(num%10)
            elif  (num>=100 and num<1000):
                result =helper(num//100) + " Hundred " +  helper(num%100)
            elif  (num>=1000 and num<1000000):
                result= helper(num//1000) + " Thousand " +  helper(num%1000)
            elif  (num>=1000000 and num<1000000000):
                result= helper(num//1000000) + " Million " +  helper(num%1000000)
            elif  (num>=1000000000):
                result= helper(num//1000000000) + " Billion " +  helper(num%1000000000)
            return result.strip()
      
        if(num==0):
            return "Zero"
        return helper(num)  
