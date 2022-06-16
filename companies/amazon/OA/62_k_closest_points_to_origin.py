# https://leetcode.com/discuss/interview-question/2092307/Amazon-OA
'''
K Closest Points to Origin
: used a max heap (~nlogk solution) and passed all test cases (although using quickselect would've yielded a better time complexity on average but I don't think it's much of a big deal as long as it's not the naive approach w/ sorting the entire array. No need to take a risk when doing an interview unless required)

Find Minimum Distance to Destination in a Grid
: a classic bfs problem. Doing a bfs while keeping track of the distance for each path yields the min distance to the destination point since bfs traverses all the connected paths from the starting point at the same time. Passed all test cases.

Got a follow-up from my recruiter about the on-site quite fast (no delay at all). Will post more about the interview experience after the on-site.
'''
