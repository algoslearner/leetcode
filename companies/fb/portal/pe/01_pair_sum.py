'''
You are given an array arr of size N. Find the number of all unique pairs in the array that sum to a number k. The elements of the array are distinct and are in sorted order.
Note: (a,b) and (b,a) are considered the same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.
Signature
int countPairs(int[] arr, int k)
Input
Array arr of N integers (Ai)
0 <= Ai <=107
2 <= N <= 107
Target sum k
0 <= k <= 107
Output
Count of all unique pairs that sum to k
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Example 1:
Input:
N = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
k = 8
Output:
3
Explanation:
We find 3 such pairs that
sum to 8: (1,7) (2,6) (3,5)
Example 2:
Input:
N = 7
arr[] = {1, 2, 3, 4, 5, 6, 7}
k = 98
Output:
0
Explanation: 
There is no pair of these numbers that sum to 98
'''

#using two pointer
# Time: O(n)
# space: O(1)

def countPairs(arr, k):
  # Write your code here
  count = 0
  j = len(arr) - 1
  
  for i in range(len(arr)):
    if i != j and j >= 0 and j < len(arr):
      if arr[i] + arr[j] == k:
        count += 1
        j -= 1
  return count
