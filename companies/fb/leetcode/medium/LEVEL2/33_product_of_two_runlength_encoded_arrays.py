'''
Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is "three 1's followed by five 2's".
The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
Compress prodNums into a run-length encoded array and return it.
You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

Return the product of encoded1 and encoded2.

Note: Compression should be done such that the run-length encoded array has the minimum possible length.

 

Example 1:

Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,6]]
Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].
Example 2:

Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
Output: [[2,3],[6,1],[9,2]]
Explanation: encoded1 expands to [1,1,1,2,3,3] and encoded2 expands to [2,2,2,3,3,3].
prodNums = [2,2,2,6,9,9], which is compressed into the run-length encoded array [[2,3],[6,1],[9,2]].
 

Constraints:

1 <= encoded1.length, encoded2.length <= 105
encoded1[i].length == 2
encoded2[j].length == 2
1 <= vali, freqi <= 104 for each encoded1[i].
1 <= valj, freqj <= 104 for each encoded2[j].
The full arrays that encoded1 and encoded2 represent are the same length.
'''

# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/discuss/1228261/Python3-Clean-two-pointers-solution
# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/discuss/1398600/Python-3-or-Two-Pointers-Clean-One-Pass-O(m%2Bn)-or-Explanation

'''
Explanation
A very straightforward solution is to
Expand result for encoded1 (O(10^5) * O(10^4) = O(10^9))
Expand result for encoded2
Calculate product of two results
Use two pointer to get the final result
Well, the issue of above solution, it will get a TLE (Time Limit Exceeded) error. O(10^9) is a time complexity even O(N) solution will get TLE. Thus, we need to do better.
A better solution, instead of expanding the encoded arrays, we can
Take 2 points on each array
Each iteration, take the shorter frequency, calculate product and add to ans
Don't forget to deduct current frequency by the smaller frequency (since it's used), and increment pointers i or j when current frequency is empty
Also, handle the situation where current product is same as the previous product
The time complexity of the above solution is O(10^5), the significance of the length of the encoded array
In the following implementation:
i: Pointer of encoded1
j: Pointer of encoded2
v1: Current value from encoded1[i]
v2: Current value from encoded2[j]
f1: Current frequency of v1
f2: Current frequency of v2
'''

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = j = f1 = f2 = v1 = v2 = 0                # Declare variables
        m, n, ans = len(encoded1), len(encoded2), []
        while i < m or j < n:                        # Starting two pointers while loop
            if not f1 and i < m:                     # If `f1 == 0`, assign new value and frequency
                v1, f1 = encoded1[i]
            if not f2 and j < n:                     # If `f2 == 0`, assign new value and frequency
                v2, f2 = encoded2[j]
            cur_min, product = min(f1, f2), v1 * v2  # Calculate smaller frequency and product
            if ans and ans[-1][0] == product:        # If current product is the same as previous one, update previous frequency
                ans[-1][1] += cur_min
            else:                                    # Other situation, append new pairs
                ans.append([product, cur_min])
            f1 -= cur_min                            # Deduct frequency by smaller frequency (used in current round)
            f2 -= cur_min
            i += not f1                              # When frequency is zero, increment pointer by 1
            j += not f2
        return ans

