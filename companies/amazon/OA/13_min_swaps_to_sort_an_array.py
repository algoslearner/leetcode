# Different wording: https://github.com/raleighlittles/Amazon-HackerRank-Assessment/blob/main/algorithm_swap/README.md

'''
I recently gave Amazon OA

no of swaps in selection sort. --- same leetcode question no of smaller elements after self -- twisted merge sort
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

https://algo.monster/problems/amazon_oa_number_of_swaps_to_sort

Given an array and a sorting algorithm, the sorting algorithm will do a selection swap. Find the number of swaps to sort the array.
Example 1:

Input: [5, 4, 1, 2]

Output: 5

Explanation:

Swap index 0 with 1 to form the sorted array [4, 5, 1, 2].
Swap index 0 with 2 to form the sorted array [1, 5, 4, 2].
Swap index 1 with 2 to form the sorted array [1, 4, 5, 2].
Swap index 1 with 3 to form the sorted array [1, 2, 5, 4].
Swap index 2 with 3 to form the sorted array [1, 2, 4, 5].

Can anyone help with O(n) solution ?
'''

# Solution: https://leetcode.com/discuss/interview-question/710751/Amazon-or-OA/914790

#My solution in JAVA , it is passing all these case :

public static int numberOfSwapsToSort(List nums) {
  Integer[] arr1 = new Integer[nums.size()];
  nums.toArray(arr1);
  int offset = 10000; // offset negative to non-negative
  int size = 2 * 10000 + 2; // total possible values in nums plus one dummy
  int[] tree = new int[size];
  List result = new ArrayList();
  
  for (int i = arr1.length - 1; i >= 0; i--) {
    int smaller_count = query(arr1[i] + offset, tree);
    result.add(smaller_count);
    update(arr1[i] + offset, 1, tree, size);
  }
  Collections.reverse(result);
    
    int sum =0;
    for(int i=0;i<result.size();i++){
        sum += result.get(i);
    }
    return sum;
}

private static void update(int index, int value, int[] tree, int size) {
    index++; // index in BIT is 1 more than the original index
    while (index < size) {
        tree[index] += value;
        index += index & -index;
    }
}

 private static int query(int index, int[] tree) {
    // return sum of [0, index)
    int result = 0;
    while (index >= 1) {
        result += tree[index];
        index -= index & -index;
    }
    return result;
}


########################################################################################################################
# https://leetcode.com/discuss/interview-question/2149341/Amazon-OA
'''
Minimum swaps to sort an array
[2, 4, 3, 1, 6] -- 3 swaps
[3, 2, 1] -- 3 swaps
[4, 7] -- 0 swap
[7, 4] -- 1 swap

I tried a couple of approaches but could not pass most test cases. :(
'''
