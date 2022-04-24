# https://leetcode.com/discuss/interview-question/1906290/Amazon-or-OA

# Related leetcode questions 1509: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# The figure reminded me of https://leetcode.com/problems/trapping-rain-water/ and the approach is similar.

#############################################################################################
# USING HEAP
# TC: O(n log n)
# SC: O(n)

import heapq

def getMinDiff(jobs, k):
    
    heapq.heapify(jobs)
    
    for _ in range(k):
        min_val = heapq.heappop(jobs)
        heapq.heappush(jobs, min_val+1)
    
    return max(jobs) - heapq.heappop(jobs)
    
    

# print 1
print(getMinDiff([2,4,3],4))
# print 6
print(getMinDiff([2,10,3],4))

# instead of using max(), you can use heapq.nlargest(1, heap). since you have transformed the list into heap

#############################################################################################
# USING trapping rainwater solution
# TC: O(n)
# SC: O(n)

'''
I think it should be possible to do better than O(Nlog(N). We can do it in O(N)

The figure reminded me of https://leetcode.com/problems/trapping-rain-water/ and the approach is similar.

First we find the max element from the array which in this case is 4. Now we alter our input array as [ 4 , 2 , 4 , 3, 4 ]
Next our objective is to fill this with water b/w the boundaries. I want to make make all the element in the array equal if possible.

Note that if the all the elements in the array are equal then the answer is simply if k % len(arr) !=0 then 1 else 0.

Here's the pseudo code in the spirit of the idea. It may not be 100% correct but I think I would try to build up on this to pass all test cases.
Please let me know if you think it would work.
'''

max_element = findMax(arr)
new_input = [max_element] + arr + [max_element] 
N = len(new_input)

left = 1
right = N - 2

while left < right:
  process_left = new_input[left]
  process_right = new_input[right] 

  if  process_left  > process_right: 
         if k > 0: 
              space_to_add = max_element - process_left
              k -= space_to_add 
             process_left+=space_to_add 
         left +=1 
    
  else:
      if k > 0: 
              space_to_add = max_element - process_right
              k -= space_to_add 
             process_right+=space_to_add 
      right-=1
    
    min_process_until_now = min(min_process_until_now , process_left,process_right) 
    max_process_until_now = max(max_process_until_now , process_left,process_right)

if k == 0:
  return max_process_until_now  - min_process_until_now  
else: 
  return 1 if  k % max_element !=0 else 0
