#
'''
Evaluate Expression (hard) #
Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

Example 1:

Input: "1+2*3"
Output: 7, 9
Explanation: 1+(2*3) => 7 and (1+2)*3 => 9
Example 2:

Input: "2*3-4-5"
Output: 8, -12, 7, -7, -3 
Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3
'''

##################################################################################################################################
# brute force - subsets
# TC: O(N * 2^N)
# SC: O(2^N)

def diff_ways_to_evaluate_expression(input):
  result = []
  # base case: if the input string is a number, parse and add it to output.
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(0, len(input)):
      char = input[i]
      if not char.isdigit():
        # break the equation here into two parts and make recursively calls
        leftParts = diff_ways_to_evaluate_expression(input[0:i])
        rightParts = diff_ways_to_evaluate_expression(input[i+1:])
        for part1 in leftParts:
          for part2 in rightParts:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()

'''
Output
0.56s
Expression evaluations: [7, 9]
Expression evaluations: [8, -12, 7, -7, -3]
'''

##################################################################################################################################
# memoization
# TC: O(N * 2^N)
# SC: O(2^N)

def diff_ways_to_evaluate_expression(input):
  return diff_ways_to_evaluate_expression_rec({}, input)


def diff_ways_to_evaluate_expression_rec(map, input):
  if input in map:
    return map[input]

  result = []
  # base case: if the input string is a number, parse and return it.
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(0, len(input)):
      char = input[i]
      if not char.isdigit():
        # break the equation here into two parts and make recursively calls
        leftParts = diff_ways_to_evaluate_expression_rec(
          map, input[0:i])
        rightParts = diff_ways_to_evaluate_expression_rec(
          map, input[i+1:])
        for part1 in leftParts:
          for part2 in rightParts:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  map[input] = result
  return result
