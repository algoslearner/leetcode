'''
About
Eight houses, represented as cells, are arranged in a straight line. Each day every cell competes with its adjacent cells (neighbors). An integer value of 1 represents an active cell and a value of 0 represents an inactive cell. If the neighbors on both the sides of a cell are either inactive or active, the cell becomes inactive on the next day; otherwise the cell becomes active. The two cells on each end have a single adjacent cell, so assume that the unoccupied space on the opposite side is an inactive cell. Even after updating the cell state, consider its previous state when updating the state of other cells. The state information of all cells should be updated simultaneously.

Write an algorithm to output the state of the cells after the given number of days.

Input
The input to the function/method consists of two arguments:

states, a list of integers representing the current state of cells after a given number of days.
days, an integer representing the number of days.
Output
Return a list of integers representing the state of the cells after a given number of days.

Note
The elements of the list states only contain either a zero or one.
'''

def cell_competition(states: list, days: int) -> list:
    new_states = []
    for day in range(0, days):
        for cell_index, cell_value in enumerate(states):
            # If you're at the beginning, treat it as though the cell that would be on your left was inactive
            if cell_index == 0:
                new_state_of_cell = determine_state_of_current_cell(0, cell_value, states[cell_index + 1])

            # Similarly, if you're at the last element, treat it as though the element that would be on your right is
            # inactive
            elif cell_index == (len(states) - 1):
                new_state_of_cell = determine_state_of_current_cell(states[cell_index - 1], cell_value, 0)

            else:
                new_state_of_cell = determine_state_of_current_cell(states[cell_index - 1], cell_value,
                                                                    states[cell_index + 1])

            new_states.append(int(new_state_of_cell))

        # update the array after each day's calculations are done
        states = new_states

        # "zero out" the new states variable
        new_states = []

    return states


def determine_state_of_current_cell(left_cell: int, current_cell: int, right_cell: int) -> int:
    return 0 if (left_cell == right_cell) else 1
  
####################################################################################################
# TEST

import unittest

import src.question_4


class TestQuestion4(unittest.TestCase):
    def test_question_4_for_a_single_day(self):
        num_days = 1
        original_array = [1, 0, 0, 0, 0, 1, 0, 0]
        output = [0, 1, 0, 0, 1, 0, 1, 0]
        self.assertEqual(src.question_4.cell_competition(original_array, num_days), output)

    def test_question_4_for_two_days(self):
        num_days = 2
        original_array = [1, 1, 1, 0, 1, 1, 1, 1, ]
        output = [0, 0, 0, 0, 0, 1, 1, 0]
        self.assertEqual(src.question_4.cell_competition(original_array, num_days), output)
