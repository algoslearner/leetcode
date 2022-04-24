# https://leetcode.com/discuss/interview-question/1602092/Amazon-or-OA-or-max-of-teams-with-Skill-difference/1165472
'''
Each team will have exactly N team size.
Skill of i th person will be denoted by skill[i] array.
Diff. between the maximum and minimum skill levels within a team cannot exeed a thershold, K.
Eg : skill = [6,1,3,4,3,5]
N = 3
K = 2

Output = 2
Explanation : Two teams can be formed [1,3,3] and [6,4,5] with difference between max and min skills not exceeding K = 2 value.

Can anyone please share the solution of this problem?

Question: Sorry, can you explain why 3,4,5 and 3,3,4 do not form a team?
Answer: Because same person can't be in two teams. There are only two person with skill 3.
'''

# double check

#############################################################################################################
# Sort, bisect, and dynamic programming to try to find a group for each worker. 
# I am pretty sure a greedy solution would work though; if I'm right about that, it would be better because it could be done in O(1) space.

from bisect import bisect_right
from functools import lru_cache

@lru_cache(None)
def helper(skill, i, n, k):
    if i % 1000 == 0:
        print(i, len(skill), n, len(skill) - n + 1)
    if i >= len(skill) - n + 1:
        return 0

    # what we get if don't use this worker
    ret = helper(skill, i + 1, n, k)

    j = min(i + n, bisect_right(skill, skill[i] + k))

    if (j - i) == n:
        ret = max(ret, helper(skill, j, n, k) + 1)
    
    return ret

def teamsWithSkillThreshold(skill, n, k):
    return helper(tuple(sorted(skill)), 0, n, k)
  
  
#############################################################################################################
def countMaxTeams(nums, teamSize, maxDiff):
  teams = 0
  n = len(nums)
  if n < teamSize:
    return teams
  
  nums.sort()
  i = 0
  while(i < n):
    if i + teamSize - 1 < n:
      diff = nums[i+teamSize-1] - nums[i]
      if diff <= maxDiff:
        teams += 1
        i += teamSize
        continue
    i += 1
  return teams
