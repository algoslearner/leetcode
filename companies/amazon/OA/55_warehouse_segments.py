# https://leetcode.com/discuss/interview-question/1655441/amazon-oa
# given an array consisting of only 1 and -1, return the max length of the subarray such that the product of all elements in said subarray is 1 

'''
Amazon warehouse has a group of n items of various wirghts lined up in a row. A segment of contiguously placed items can be shipped ogether if only if the difference betweeen the weihts of the heaviest and lightest item differs by at most k to avoid load imbalance.

Given the weights of the n items and an integer k, fine the number of segments of items that can be shipped together.

Note: A segment (l,r) is a subarray starting at index l and ending at index r where l less than equal(<=) r.
Example
k=3
weights = [1, 3, 6]
weight difference between max and min for each (l,r) index pair are:
(0,0) -> max(weights[0]) - min(weights[0]) = max(1)-min(1) = 1-1 =0
(0,1) - > max(weights[0],weights[1]) - min(weights[0],weights[1])= max(1,3)-min(1,3)=3-1=2
(0,2) - > max(weights[0],weights[1],weights[2]) - min(weights[0],weights[1],weights[2])= max(1,3,6)-min(1,3,6)=6-1=5
(1,1) -> max(weights[1]) - min(weights[1]) = max(3)-min(3) = 3-3 =0
(1,2) -> max(weights[1],weights[2]) - min(weights[1],weights[2]) = max(3,6)-min(3,6) = 6-3 =3
(2,2) -> max(weights[2])-min(weights[2]) = max(6)-min(6) = 6-6 =0

as only 5 out 6 pair, is less than equal equal to k (3) , so the number of segemets that can shipped together is 5.
Constraints
1<=k, weights[i] <=10^9
1 <= n <=3*10^5
'''

# Similar to https://leetcode.com/problems/sum-of-subarray-ranges/
# It's similar to 239. Sliding Window Maximum. https://leetcode.com/problems/sliding-window-maximum/
# https://ideone.com/sN8H2F the problem simplifies to finding sum of cnt(a[i]-k <= a[j]) such that j < i
