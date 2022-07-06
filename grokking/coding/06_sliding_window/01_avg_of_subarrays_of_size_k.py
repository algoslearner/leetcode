# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
'''
Let’s understand this problem with a real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here, we are asked to find the average of all subarrays of ‘5’ contiguous elements in the given array. Let’s solve this:

For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2
(1+3+2+6−1)/5=>2.2
The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5 => 2.8
(3+2+6−1+4)/5=>2.8
For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4
(2+6−1+4+1)/5=>2.4

…
Here is the final output containing the averages of all subarrays of size 5:

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
'''

###########################################################################################################
# brute force
# TC: O(nk)
# SC: O(1)

def find_averages_of_subarrays(arr, k):
  output = []
  for i in range(len(arr) - k + 1):
    sub_sum = 0.0
    for j in range(i, i + k):
      sub_sum += arr[j]
    output.append( sub_sum / k)
  return output

###########################################################################################################
# sliding window
# TC: O(n)
# SC: O(1)

def find_averages_of_subarrays(arr, k):
  output = []
  sub_sum = 0.0
  start = 0
  
  for end in range(len(arr)):
    sub_sum += arr[end]
    
    # slide the window
    if end >= k - 1:
      output.append( sub_sum / k)
      sub_sum -= arr[start]
      start += 1
      
  return output
  
