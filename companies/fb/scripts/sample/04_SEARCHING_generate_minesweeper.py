'''
Searching algorithms
 1. (*high frequency question) Generate a minesweeper grid (2x3) with 3 randomly-placed mines (solution)

Implement Minesweeper
Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid. 
You are given a uniform grid of gray squares in the beginning of the game. 
Each square contains either a mine (indicated by a value of 9), or an empty square. 
Empty squares have a number indicating the count of mines in the adjacent squares. 
Empty squares can have counts from zero (no adjacent mines) up to 8 (all adjacent squares are mines).
If you were to take a complete grid, for example, you can see which squares have mines and which squares are empty:

'''
##############################################################################################################
# https://techdevguide.withgoogle.com/resources/former-interview-question-minesweeper/
# create a minesweeper class
'''
Simple class
This question definitely points towards designing a simple class.
Create an array with the specified number of mines at the beginning and use a random shuffle.
If mines occupy more than half of the cells, randomize empty cells instead of mines.

If for NxN you need M mines then:
1) if M < NxN/2 then randomly pick spots and if empty place mines. At worst, the chance of picking a mine rather than empty cell is 50% so we need 2M tries.
2) if M > NxN/2 try step 1 assuming that all cells are mined and we are trying to free up (NxN - M) spots. So in the extreme example above, it takes almost one try

What is the right way to report a problem if the requested number of mines is larger than the number of available squares?
'''

##### LEARNINGS
'''
For the initialization, you might choose to place mines and increment neighbors in one loop, 
or place mines and then iterate over all fields and count the mines in the neighborhood.

A common error is to struggle to see the structure of the problem and make gigantic if clauses when looking at neighboring fields, 
instead of writing a simple for loop.

An important part of this question is figuring out a way to place the mines. 
The most naive implementation is to pick two random numbers (row and column) and place a mine there, 
but this will cause the board to have less mines than expected if the same coordinates are picked twice. 

Re-trying if the picked coordinates already have a mine fixes the immediate problem, 
but will take a very long time for cases such as a 100x100 board with 9999 mines.
'''


import random
kMine = 9
class Matrix():
  def __init__(self, T):
    self.elem_type = T
  def resize(self, rows, cols):
    self.data = [self.elem_type() for _ in range(rows * cols)]
    self.rows, self.cols = rows, cols
  def at(self, row, col):
    return self.data[row * self.cols + col]
  def rows(self):
    return self.rows
  def cols(self):
    return self.cols
class MineField():
  class Spot():
    def __init__(self):
      self.value = 0
      self.visible = False
  def _spot(self):
    return self.Spot()
  def __init__(self, rows, cols, num_mines):
    self.matrix = Matrix(self._spot)
    self.matrix.resize(rows, cols)
    self.rows, self.cols = rows, cols
    if num_mines > rows * cols:
      print("Too many mines")
    mine_list = [i < num_mines for i in range(rows * cols)]
    random.shuffle(mine_list)
    print(mine_list)
    for index, is_mine in enumerate(mine_list):
      if not is_mine:
        continue
      row, col = index // cols, index % cols
      self.matrix.at(row, col).value = kMine
      for i in range(-1, 2):
        for j in range(-1, 2):
          if row + i < 0 or row + i >= rows or col + j < 0 or col + j >= cols:
            continue
          if self.matrix.at(row + i, col + j).value == kMine:
            continue
          self.matrix.at(row + i, col + j).value += 1
  def OnClick(self, row, col):
    if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
      return False
    spot = self.matrix.at(row, col)
    if spot.visible:
      return False
    spot.visible = True
    if spot.value == kMine:
      print("Boom!!!!

")
      return True
    if spot.value != 0:
      return False
    self.OnClick(row - 1, col)
    self.OnClick(row, col - 1)
    self.OnClick(row + 1, col)
    self.OnClick(row, col + 1)
    return False
  def Print(self, show_hidden=False):
    for i in range(self.rows):
      for j in range(self.cols):
        ch = '.'
        if self.matrix.at(i, j).visible or show_hidden:
          ch = self.matrix.at(i, j).value
        print(ch, end=' ')
      print()
    print()
    print()
if __name__ == '__main__':
  mine_field = MineField(12, 10, 7);
  mine_field.Print(True);
  mine_field.OnClick(5, 2);
  mine_field.Print();
  mine_field.OnClick(2, 6);
  mine_field.Print();
  mine_field.OnClick(9, 3);
  mine_field.Print();
  mine_field.OnClick(0, 0);
  mine_field.Print();
  mine_field.OnClick(3, 5);
  mine_field.Print();
            
