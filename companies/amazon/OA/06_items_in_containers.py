##########################################################################################################
# Amazon OA question: https://leetcode.com/discuss/interview-question/1180017/Amazon-OA/1171090
'''
prob 2:
https://leetcode.com/discuss/interview-question/1148760/items-in-containers-amazon-oa
* and | problem. Given a string with * and | and 2 arrays of startIndices and endIndices, output an array of the number of compartments (between 2 sticks)
*|**| has 1 compartment with 2 *.
Doable in O(N) time.

#######################################Problem 2 Statement and Soln:
An item is represented as an asterisk ( * = ascii decimal 42). A compartment is represented as a pair of pipes that may or may not have items between them ( | = ascii decimal 124).

Example 1:
Input: s = |**|*|*, startIndices = [1, 1], endIndices = [5, 6]
Output: [2, 3]
Explanation:
The string has a total of 2 closed compartments, one with 2 items and one with 1 item.
For the first pair of indices, (0, 4), the substring |**|*. There are 2 items in a compartment.
For the second pair of indices, (0, 6), the substring is |**|*|* and there are 2 + 1 = 3 items in compartments.
Both of the answers are returned in an array, [2, 3]
Example 2:
Input: s = *|*|, startIndices = [1], endIndices = [3]
Output: [1]
Explanation:
the substring from index = 1 to index = 3 is |*|. There is one compartments with one item in this string.
Constraints:
1 <= m, n <= 10^5
1 <= startIndices[i] <= endIndices[i] <= n
Each character or s is either * or |
'''


##########################################################################################################
# O(N) solution

def cntitems2(items: str, startIndices: List[int], endIndices: List[int]) -> List[int]:
    ln = len(items)
    # pre-calc left-most pipe location and sum of stars arrays
    stars = [0] * (ln+1)
    lftpipeidx = [-1] * (ln+1)
    for i, ch in enumerate(items,1):
        if ch == "|":
            stars[i] = stars[i-1]
            lftpipeidx[i] = i
        else:  # ch == *
            stars[i] = stars[i-1] + 1
            lftpipeidx[i] = lftpipeidx[i-1]
    if lftpipeidx[-1] == -1:
        return [0]*len(startIndices)

    # pre-calc right-most pipe location
    rgtpipeidx = [ln+1] * (ln+1)
    for i in range(ln-1,-1,-1):
        if items[i] == '|':
            rgtpipeidx[i+1] = i+1
        else:
            rgtpipeidx[i+1] = rgtpipeidx[i+2] if i < ln-1 else ln+1

    # calc answer as difference between num. of stars b/w right and left pipes.
    # right pipe is the left-most pipe from the end index, left pipe is the right-most one from the start index
    ans = []
    for i in range(len(startIndices)):
        si, ei = startIndices[i], endIndices[i]
        lftpipe = rgtpipeidx[si]
        rgtpipe = lftpipeidx[ei]
        ans.append(stars[rgtpipe] - stars[lftpipe] if lftpipe < rgtpipe else 0)
    return ans


if __name__ == '__main__':
    #  1-based index, assume start idx <= end idx, and both indices within the range 1..ln
    print(cntitems2("|**|*|*",[1,1,2],[5,7,7]))  # [2, 3, 1]
    print(cntitems2("*|**|*|**|****|*",[4,1,4],[8,16,11]))  # [1, 9, 3]
    print(cntitems2("*****|*****",[1,4,1,7],[5,8,11,9]))  # [0, 0, 0, 0]


##########################################################################################################
# O(NlogN) old solution:

from typing import List
from collections import Counter
import bisect

# assume len(startIndices) == len(endIndices)
def cntitems(items: str, startIndices: List[int], endIndices: List[int]) -> List[int]:
    pipes,stars = [],0
    pdic = Counter()
    for i, ch in enumerate(items):
        if ch == "|":
            pdic[i] = stars
            pipes.append(i)
        elif pipes: # ch == *
            stars += 1
    if not pipes:
        return [0]*len(startIndices)

    ans = []
    for i in range(len(startIndices)):
        si,ei = startIndices[i],endIndices[i]
        spi = bisect.bisect_left(pipes,si)
        epi = bisect.bisect_right(pipes,ei)-1
        ans.append(pdic[pipes[epi]] - pdic[pipes[spi]])
    return ans


if __name__ == '__main__':
    # 0-based index
    print(cntitems("|**|*|*",[0,0,1],[4,6,6]))  # [2, 3, 1]
    print(cntitems("*|**|*|**|****|*",[3,0,3],[7,100,10]))  # [1, 9, 3]
    print(cntitems("*****|*****",[3,0,3],[7,100,10]))  # [0, 0, 0]
    
    
##########################################################################################################
# O(N) solution : Java working solution
'''
@kheman the solution is working and passed all the test cases. Change below code only.
int start = startIndices.get(i)-1;
int end = endIndices.get(i)-1;
'''

public List<Integer> numberOfItems(String s, List<Integer> startIndices, List<Integer> endIndices) {
        int n = s.length();
        int[] dp = new int[n];
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '|') {
                dp[i] = count;
            } else {
                count++;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < startIndices.size(); i++) {
            int start = startIndices.get(i);
            int end = endIndices.get(i);

            while (s.charAt(start) != '|') start++;
            while (s.charAt(end) != '|') end--;
            if (start < end) {
                ans.add(dp[end] - dp[start]);
            } else {
                ans.add(0);
            }
        }
        return ans;
    }

##########################################################################################################
# Similar leetcode question: problem2 : https://leetcode.com/problems/plates-between-candles/
'''
2055. Plates Between Candles

There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:

ex-1
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
Example 2:

ex-2
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
 

Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length
'''

#########################################################################################################################
# binary search + hashmap
# TC: O(N + Q log N)
# SC: O(N)

import bisect
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # count the number of plates:
        count = 0
        hashmap = collections.defaultdict()
        pos = []
        for i, c in enumerate(s):
            if c == "*":
                count += 1
            if c == '|':
                hashmap[i] = count
                pos.append(i)
                
        result = [0]*len(queries)
        # retrieve by queries
        for i, (l, r) in enumerate(queries):
            # use binary search of the left and right commands
            idx_l = bisect.bisect_left(pos, l)
            idx_r = bisect.bisect_right(pos, r) - 1
            if (idx_l >= idx_r) or (idx_l < 0) or (idx_r >= len(pos)):
                continue
            l = pos[idx_l]
            r = pos[idx_r]
            result[i] = hashmap[r] - hashmap[l]
        # time: O(N + Q*logN)
        # space: O(N)
        return result

