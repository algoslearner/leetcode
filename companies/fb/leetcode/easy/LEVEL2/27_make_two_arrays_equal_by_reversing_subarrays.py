'''
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.
 

Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
'''

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # TC : O(n log n)
         return sorted(target) == sorted(arr)
  
  '''
Sure you can do it in 1-line using library methods, but if you do that on the interview you will get a follow up question how to do it without the library.
So here you go: '''

# IDEA: if we can make them equal that means they contain same numbers in same quantities
#       build dictionary with target counts, then iterate over input array making sure that counts match
#       O(N) time, O(N) space
#
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = collections.defaultdict(int)
        for t in target:
            counter[t] += 1
        for a in arr:
            if a not in counter or counter[a] == 0:
                return False
            counter[a] -= 1
        return all(v == 0 for v in counter.values())
