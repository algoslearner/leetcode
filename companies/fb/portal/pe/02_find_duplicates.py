'''
Given an array arr[] of size N which contains elements from 0 to N-1, find all the elements occurring more than once in the given array.
Signature
int[] findDuplicates(int[] arr)
Input
An array arr of size N where
1 <= N <= 105
0 <= arr[i] <= N-1, for each valid i
Output
A sorted list of elements that occur more than once. If no such element is found, return {}.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Note: The extra space is only for the array to be returned. Try and perform all operation within the provided array.
Example 1:
Input:
N = 4
arr[] = {0,3,1,2}
Output: 
{}
Explanation: 
N = 4 and all elements from 0 to (N-1 = 3) are present in the given array. Therefore output is {}.
Example 2:
Input:
N = 5
arr[] = {2,3,1,2,3}
Output: 
{2, 3}
Explanation: 
2 and 3 occur more than once in the given array.
'''

# TC : O(n)
# SC : O(n)
def findDuplicates(arr):
  # Write your code here
  arr.sort()
  output = []
  for i in range(len(arr)):
    if i != 0:
      if arr[i-1] == arr[i]:
        output.append(arr[i-1])
  
  return output
