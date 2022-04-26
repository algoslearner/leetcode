#https://leetcode.com/discuss/interview-question/347457/Amazon-or-OA-2019-or-Treasure-Island
'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''
# Similar to this one: https://leetcode.com/problems/walls-and-gates/
####################################################################################################
# Java BFS: https://leetcode.com/playground/uQoVfEmr
# Time complexity: O(r * c).
# Space complexity: O(r * c).

print("Treasure Island - Amazon online Assessment")
print('')

'''
Approach - 1 - using adjList to represent the board
Steps:
    1 - build adj list graph
    2 - BFS using queue q = [(x,y)]
    3 - steps counter
 ----------
Compelxity:
time : O(L^2) where N is the map's dimension
space : O(N) where N is the number of safe/navigable cells pre-processed (stored) in the adj-list dict 
'''
def func1(M):
    # Build adj list for coordinates
    from collections import defaultdict
    d = defaultdict(list)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != 'D':
                # no need to store the link the other way around. It's done implcity due to looping over cells
                if i+1 <= len(M)-1:
                    d[(i,j)].append((i+1,j)) 
                if i-1 >= 0:
                    d[(i,j)].append((i-1,j))
                if j+1 <= len(M[i])-1:
                    d[(i,j)].append((i,j+1))
                if j-1 >= 0:
                    d[(i,j)].append((i,j-1))
  
    from collections import deque
    q = deque()
    q.append((0,0)) # top-left = start
    steps = 0
    visited = set()
    while q:
        for i in range(len(q)):
            node = q.popleft() # node = (x,y)
            
            if M[node[0]][node[1]] == 'X':
                return steps
            
            for n in d[node]:
                if n not in visited:
                    if M[n[0]][n[1]] != 'D': # safe to sail or if lucky treasure
                        q.append((n))
                        visited.add(n)
                        d[n].remove(node)
            del d[node]
        steps += 1
    return steps

'''
Approach - 2 -
Instead of using dict - adj list and do BFS on that,
i could start my queue with (0,0) in it and then
use a list of dirs to figure our the neighbours
----------
Compelxity:
time : O(E+V) E, V = edges, vertcies
space : O(1) at any given time, queue holds 4 cells at max. No other DS are used.
'''
def func2(M):
    from collections import deque
    q = deque()
    q.append((0,0))
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    steps = 0
    visited = set()
    visited.add((0,0))
    while q:
        for i in range(len(q)):
            node = q.popleft()
            x, y = node[0], node[1]
            
            if M[x][y] == 'X':
                return steps
            
            for dir in dirs: # inseatd of looping over d[node]
                newX, newY = x+dir[0], y+dir[1]
                # check bounds:
                if newX >= 0 and newX <= len(M)-1 and newY >= 0 and newY <= len(M[0])-1:
                    # check cell:
                    if M[newX][newY] != 'D':
                        # check if visited:
                        if (newX, newY) not in visited:
                            q.append((newX, newY))
                            visited.add((newX, newY))
        steps += 1
    return steps
    
M = [['O', 'O', 'O', 'O'],['D', 'O', 'D', 'O'],['O', 'O', 'O', 'O'],['X', 'D', 'D', 'O']]
print('>> Using an adj list and BFS <<')
print(func1(M))
print('>> Using dirs and BFS <<')
print(func2(M))

####################################################################################################
# DFS : Failed 20% of testcases in interview site
# Time complexity: 
# Space complexity: 

def find_treasure(t_map, row, col, curr_steps, min_steps):
    if row >= len(t_map) or row < 0 or col >= len(t_map[0]) or col < 0 or t_map[row][col] == 'D' or t_map[row][col] == '#':
        return None, min_steps

    if t_map[row][col] == 'X':
        curr_steps += 1
        if min_steps > curr_steps:
            min_steps = min(curr_steps, min_steps)

        return None, min_steps

    else:
        tmp = t_map[row][col]
        t_map[row][col] = '#'
        curr_steps += 1
        left = find_treasure(t_map, row, col-1, curr_steps, min_steps)
        right = find_treasure(t_map, row, col+1, curr_steps, min_steps)
        up = find_treasure(t_map, row-1, col, curr_steps, min_steps)
        down = find_treasure(t_map, row+1, col, curr_steps, min_steps)

        t_map[row][col] = tmp

        return curr_steps, min(left[1], right[1], up[1], down[1])


if __name__ == '__main__':
 #    treasure_map = [['O', 'O', 'O', 'O'],
 # ['D', 'O', 'D', 'O'],
 # ['O', 'O', 'O', 'O'],
 # ['X', 'D', 'D', 'O']]
    treasure_map = [['O', 'O', 'O', 'X'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O']]

    res = find_treasure(treasure_map, 0, 0, -1, float('inf'))
    print("Result: ", res[1])
