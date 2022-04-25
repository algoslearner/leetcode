# https://leetcode.com/discuss/interview-question/1402110/Amazon-OA

'''
Two questions (105 mins)

Fleet of vehicles - https://leetcode.com/discuss/interview-question/1365052/Amazon-OA
https://leetcode.com/problems/rank-transform-of-an-array/ but worded differently
SDE II, USA
'''

'''
Need to loop over the input array and then for each number they want you to dish out the total ways call the countsubsetsum method.
Use https://leetcode.com/problems/coin-change-2/ for the base problem.
'''

#Fleet of vehicles: Can be done using unbounded knapsack
    def countsubsetsum(coins, n, amount):
        t = [[0 for i in range(amount+1)] for i in range(n+1)]
        for row in t:
            row[0] = 1
        
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                
                if coins[i-1] <= j:
                   t[i][j] = t[i-1][j] + t[i][j-coins[i-1]]
                else:
                    t[i][j] = t[i-1][j]
                    
        return t[n][amount]

for num_wheels in ip:
    ans = []
    wheels = [2,4]
    ans.append( countsubsetsum(wheels, n, num_wheels) )
