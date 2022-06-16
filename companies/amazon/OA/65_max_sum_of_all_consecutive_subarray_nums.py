# https://leetcode.com/discuss/interview-question/2023674/Amazon-OA
'''
Given an array consisting of N integer and two number k,d.
Task1-From the given array we can choose k consecutive elements one after in array and after that leave an array element.Then we calculate maximum sum of all such consecutive element containing subarray.
Task2-From the given array we can choose k+d consecutive elements one after in array and after that leave an array element.Then we calculate maximum sum of all such consecutive element containing subarray.
Find the difference between task1 and task 2 ans.
ex 1->arr=[1,2,3,4,8,9,10]
k=2,d=1;
Task1 elements {3,4}+{9,10}=7+19=26
Task2 elements {1,2,3}+{8,9,10}=6+27=33;
output=33-26=7
'''


########################################################################################################
# solution 1
'''
Can be solved using DP:

/*
1. Pre-compute prefix sum in advance to get sum of k/k+d continuous elements.
2. For each element in given array, it has 2 choices, whether be the start of next k-1 continuous elements sum or just skip itself.
3. Get the max of both inclusion and exclusion case and memoize it.
4. Call the function again for k+d and return the difference of both tasks.
*/

int maxSum(vector<int>&prefix_sum, vector<int>&dp, int k, int index)
{
  if(index >= dp.size() || index + k -1 >= dp.size())
      return 0;
  
  if(dp[index] != INT_MIN)
      return dp[index];
  
  int include = 0, exclude = 0;
  include = maxSum(prefix_sum, dp, k, index + k + 1) + prefix_sum[index + k] - prefix_sum[index]; 
  exclude = maxSum(prefix_sum, dp, k, index + 1);
  return dp[index] = max(include, exclude);
}

int getDIff(vector<int>&nums, int k, int d)
{
  int n = nums.size();
  vector<int>dp_1(n, INT_MIN), dp_2(n, INT_MIN), prefix_sum(n + 1, 0);
  
  for(int i = 1; i <= n; i++)
      prefix_sum[i] = prefix_sum[i-1] + nums[i-1];
  
  int sum_1 = maxSum(prefix_sum, dp_1, k, 0);
  int sum_2 = maxSum(prefix_sum, dp_2, k+d, 0);
  return abs(sum_2 - sum_1);
}
'''
