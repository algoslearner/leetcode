'''
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 

Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104
'''

###############
'''
Explanation
Take K as a carry.
Add it to the lowest digit,
Update carry K,
and keep going to higher digit.


Complexity
Insert will take O(1) time or O(N) time on shifting, depending on the data stucture.
But in this problem K is at most 5 digit so this is restricted.
So this part doesn't matter.

The overall time complexity is O(N).
For space I'll say O(1)
'''
def addToArrayForm(self, A, K):
        for i in range(len(A) - 1, -1, -1):
            K, A[i] = divmod(A[i] + K, 10)
        return [int(i) for i in str(K)] + A if K else A

# If A is very large, K is not that large, we can just stop when K->0
# We should always convert K into list, so the iteration should be of the size of K
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        B = []
        while k:
            a = num.pop() if num else 0
            k += a
            k, r = divmod(k, 10)
            B.append(r)
        B.reverse()
        return num+B

