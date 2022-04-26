'''
About
Amazon is planning to release a new order prioritization algorithm to optimize fulfilling Prime deliverise on time. 
All orders (Prime or otherwise) are given an alphanumeric ID code. 
However, Prime orders are given additional metadata that consists of a space delimited string of positive integers. 
Each order is therefore defined as their alphanumeric ID code, followed by a space, followed by their space delimited metadata.

You have been tasked with sorting a list of all orders in the order queue to assist in prioritization of fulfillment. 
They should be sorted according to the following order.

The prime orders should be returned first, sorted by lexigraphic sort of the alphabetic metadata.
Only in the case of ties, the identifier should be used as a backup sort.
The remaining non-Prime orders must come after, in the original order they were given in the input.
Write a function or method to sort the orders according to this pattern.

Input
The input to the function/method consists of two arguments; num_orders is an integer representing the number of orders. order_list, a list of strings representing all of the orders.

Output
Return a list of strings representing the correctly prioritized orders.

Note
The order identifier consists of only lower case English characters and numbers.
'''

def sortOrders(num_orders: int, order_list: list) -> list:
    # Like the question says, prime orders should come first, and then within the prime orders
    # sort over the metadata, which is everything after the identifier.
    prime_orders: list = sorted(filter(is_prime_order, order_list), key=lambda k: (k.split()[1:], k.split()[0]))

    # Non-Prime orders
    non_prime_orders: list = list(filter(lambda v: not is_prime_order(v), order_list))

    return prime_orders + non_prime_orders


def is_prime_order(order_info: str) -> bool:
    return order_info.split()[1].isalpha()
  
  
#########################################################
# TEST

import unittest
import src.question_1

class TestQuestion1(unittest.TestCase):
    def test_question_1(self):
        num_orders = 6
        orderList = ["zld 93 12",
                     "fp kindle book",
                     "10a echo show",
                     "17g 12 25 6",
                     "ab1 kindle book",
                     "125 echo dot second generation"]

        expectedOutput = ["125 echo dot second generation",
                          "10a echo show",
                          "ab1 kindle book",
                          "fp kindle book",
                          "zld 93 12",
                          "17g 12 25 6"]

        self.assertEqual(src.question_1.sortOrders(num_orders, orderList), expectedOutput)

## Explanation
# There are four 4 prime orders (lines with words) in this order list. Because "echo" comes before kindle, those lines should come first, with "dot" coming before "show". Because two lines have the same metadata -- "kindle book", their tie should be broken by the identifier, where "ab1" comes before "fp". Finally, the non-Prime numeric orders should come last, in their original order as they were in the input.




