# https://leetcode.com/discuss/interview-question/1505615/Amazon-OA
'''
Get the sum of min and max diff for all subarrays

[2,4,3,5]

wrong: sum = (4 - 2) + (4 - 3) + (5 - 3) + (3 - 2) + (5 - 4) + (5 - 2) = 10
sum = (4 - 2) + (4 - 3) + (5 - 3) + (4 - 2) + (5 - 3) + (5 - 2) = 12

O(n2) exceeds time limit
Not sure how to optimize to be < O(n2)
I used mono queue. but failed to passed test case starting from 7
I was using long and appply mod . but it doesn't help .

answer is Sum of subarray maximums - Sum of subarray minimums.
Similar Ques: https://leetcode.com/problems/sum-of-subarray-minimums/

The above question is same as https://leetcode.com/problems/sum-of-subarray-ranges/
Got it in my OA
'''

# O(n) solution idea
# https://leetcode.com/playground/BnHvortJ

#[2,4,3,5]
def  sumSubarrayMin(arr) : 
    stack = []
    arr.append(-1) 
    res=0  
    
    for i in range(len(arr))  :  
        while stack and  arr[i] <  arr[stack[-1]] : 
            idx = stack.pop() 
            res+=  arr[idx] *  (i-idx ) *  (idx -  (stack[-1] if stack else -1 ))
        stack.append(i) 
    return res % (10 **9  +7) 

def  sumSubarrayMax(arr) : 
    stack = []
    arr.append(float('inf')) 
    res=0  
    
    for i in range(len(arr))  :  
        while stack and  arr[i] >  arr[stack[-1]] : 
            idx = stack.pop() 
            res+=  arr[idx] *  (i-idx ) *  (idx -  (stack[-1] if stack else -1 ))
        stack.append(i) 
    return res % (10 **9  + 7 )

minn = sumSubarrayMin([2,4,3,5])
maxx= sumSubarrayMax([2,4,3,5])
print(maxx -minn)

# output = 12


