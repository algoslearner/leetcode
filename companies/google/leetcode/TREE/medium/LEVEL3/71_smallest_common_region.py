# https://leetcode.com/problems/smallest-common-region/
'''
1257. Smallest Common Region

You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region x contains another region y then x is bigger than y. Also, by definition, a region x contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If you are given regions r1, r2, and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It is guaranteed the smallest region exists.

 

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
Example 2:

Input: regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"
Output: "Earth"
 

Constraints:

2 <= regions.length <= 104
2 <= regions[i].length <= 20
1 <= regions[i][j].length, region1.length, region2.length <= 20
region1 != region2
regions[i][j], region1, and region2 consist of English letters
'''

################################################################################################
# HASHSET
# TC: O(N), N is the number of total regions
# SC: O(N)
# https://leetcode.com/problems/smallest-common-region/discuss/430500/JavaPython-3-Lowest-common-ancestor-w-brief-explanation-and-analysis.

'''
Build family tree from offsprings to their parents;
Use a HashSet to construct ancestry history of region1;
Retrieve ancestry of region2 by family tree till find the first common ancestry in ancestry history of region1.
'''

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {region[i] : region[0] for region in regions for i in range(1, len(region))}
        ancestry_history = {region1}
        while region1 in parents:
            region1 = parents[region1]
            ancestry_history.add(region1)
        while region2 not in ancestry_history:
            region2 = parents[region2]
        return region2
