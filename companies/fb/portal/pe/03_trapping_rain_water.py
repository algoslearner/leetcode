'''
Given an array arr[] of N non-negative integers representing the height of blocks lined up directly next to each other, if the width and depth of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
Note: Water is trapped only on top of blocks when there are boundaries to both the right and left of the blocks.
Signature
int getTrappedRainWater(int[] arr)
Input
Array arr of N integers (Ai)
3 <= N <= 107
0 <= Ai <= 108
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Example 1:
Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Block of height 4 has 3 units on top of it bordering the block of height 7, since that is shorter than the block of height 9.
Block of height 0 has 7 units on top of it bordering the block of height 7, since that is shorter than its other border, the block of height 9.
Total units of water trapped is 10 units.
Example 2:
Input:
N = 3
arr[] = {6,9,9}
Output:
0
Explanation:
No water will be trapped, as there is no space to trap it.
'''

