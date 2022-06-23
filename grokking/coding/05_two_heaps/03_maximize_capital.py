#
'''
Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the most profitable projects.

We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.

Example 1:

Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
Output: 6
Explanation:

With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we selected our first project, our total capital will become 3 (profit + initial capital).
With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
After the completion of the two projects, our total capital will be 6 (1+2+3).

Example 2:

Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0, Number of Projects=3
Output: 8
Explanation:

With ‘0’ capital, we can only select the first project, bringing out capital to 1.
Next, we will select the second project, which will bring our capital to 3.
Next, we will select the fourth project, giving us a profit of 5.
After selecting the three projects, our total capital will be 8 (1+2+5).
'''

###################################################################################################################
# two heaps
# TC: O(N log N + K log N)
# SC: O(N)

from heapq import *

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
  minCapitalHeap = []
  maxProfitHeap = []
        
  # add all projects into minheap, to find a project with min capital
  for i in range(0, len(profits)):
    heappush(minCapitalHeap, (capital[i], i))
            
    # find projects which are affordable
    available_capital = initialCapital
    for _ in range(numberOfProjects):
      while minCapitalHeap and minCapitalHeap[0][0] <= available_capital:
        capital, i = heappop(minCapitalHeap)
        heappush(maxProfitHeap, (profits[i], i))
      if not maxProfitHeap:
        break
      available_capital += -heappop(maxProfitHeap)[0]

    return available_capital

def main():
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()

'''
Output 0.86s

Maximum capital: 0
Maximum capital: -1
'''
