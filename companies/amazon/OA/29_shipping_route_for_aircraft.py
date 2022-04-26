'''
About
Amazon Prime Air is developing a system that divides shipping routes using flight optimization routing systems to a cluster of aircraft that can fulfill these routes. Each shipping route is identified by a unique identifier and requires a fixed non-zero amount of travel distance between airports, and is defined to be either a 'forward' or a 'backward' route. Identifiers are guaranteed to be unique within their own route type, but not across route types.

Each aircraft should be assigned two shipping routes at once: one forward route and one return route. Due to the complex scheduling of flight plans, all aircraft have a fixed maximum operating travel distance, and cannot be scheduled to a fly a route that exceeds this maximum distance. The goal of the system is to optimize the total operating travel distance of a given aircraft. A forward/return shipping route pair is considered to be "optimal" if there den airportsnot exist another pair that has a higher operating travel distance than this pair, and also has a total less than or equal to the maximum safe travel disen airportse of the aircraft.

For example, if the aircraft has a maximum operating travel distance of 3,000 miles, a forward return shipping route pair using a total of 2998 milesen airportsld be optimal if there does not exist a pair that uses a total operating distance of 2999 miles -- but would not be optimal if such a pair did in fact een airports.

Your task is to write an algorithm to optimize the sets of forward/return shipping route pairs that allow the aircraft to be optimally utilized, given a list of forward shipping routes and a list of return shipping routes.en airports

Input
The input to the function/method consists of three arguments: maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft; forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping route and the second integer represents the amount of travel distance of required by this shipping route. returnRouteList, a list of pairs of integers where the first integer represents the unique identifier of a return shipping route and the second integer represents the amount of travel distance required by this shipping route.

Output
Return a list of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft. If no route is possible, return a list with empty pair.
'''

###################################################
# SOLUTION

def optimalUtilization(maxTravelDist: int, forwardRouteList: list, returnRouteList: list) -> list:
    """
    Sort both list of routes by their distance, in decreasing order.
    Then discard any route greater than or equal to the maximum travel distance.
    Then, pick the longest route in the forward direction. (Either direction would work here)
    Once you have the longest forward route, go down the list of returning routes (in sorted order),
    and make sure that the distance of the forward route you picked earlier plus the distance of
    the current returning route does not exceed the safe travel distance.
    If you find a pair whose sum does not exceed the safe travel distance, store that as the best
    route pair.
    Keep repeating this process as you go down the current list of returning routes. Once you've
    performed this process for all return routes for the given forward route you chose, move
    on to the next longest route. If the distance of the forward route plus the distance of the
    return route do not exceed the length of the best distance, then keep going (remember that the routes are sorted!)
    :param maxTravelDist:
    :param forwardRouteList:
    :param returnRouteList:
    :return:
    """
    optimal_route_pairs = []
    best_distance = 0

    sortedForwardRoutes = sorted(forwardRouteList, key=lambda k: k[1], reverse=True)
    sortedReturnRoutes = sorted(returnRouteList, key=lambda k: k[1], reverse=True)

    for forward_route in sortedForwardRoutes:
        fwd_route_id, fwd_route_length = forward_route

        if fwd_route_length >= maxTravelDist:
            # Skip this forward route if it is greater than or equal to the maximum distance
            # If this route is exactly equal to the maximum distance, then you wouldn't have
            # enough "fuel" to make the return leg of the journey.
            continue

        for return_route in sortedReturnRoutes:
            ret_route_id, ret_route_length = return_route

            # Have you found the best distance yet?
            if (best_distance == 0):
                # If not, check if this route could be your best distance.
                if (fwd_route_length + ret_route_length) <= maxTravelDist:
                    # If you haven't found a best distance yet, and the sum of these route lengths
                    # are within your safe travel distance, then this is your best route (for now).
                    best_distance = fwd_route_length + ret_route_length
                    optimal_route_pairs.append([fwd_route_id, ret_route_id])

                else:
                    # If this combination of forward route and return route are longer than the max
                    # travel distance, then go on to the next longest return route
                    continue


            else:
                # If you've seen a best distance so far, check if this route exceeds that distance
                if (fwd_route_length + ret_route_length) < best_distance:
                    # If this combined route length doesn't match your best distance, then it can't
                    # be in the optimal set; and further, since you've been iterating over the trips
                    # sorted by length first, by the time you reach here, you are done, there cannot be another optimal path.
                    break

                elif (fwd_route_length + ret_route_length == best_distance):
                    optimal_route_pairs.append([fwd_route_id, ret_route_id])

    return optimal_route_pairs
  

#################################################################
# TEST

import unittest

import src.question_2


class TestQuestion2(unittest.TestCase):
    def test_question_2_where_there_is_only_optimal_route(self):
        max_travel_distance = 7000

        forwardRouteList = [[1, 2000],
                            [2, 4000],
                            [3, 6000]]

        returnRouteList = [[1, 2000]]

        output = [[2, 1]]

        self.assertEqual(src.question_2.optimalUtilization(max_travel_distance, forwardRouteList, returnRouteList),
                         output)
        ##  Explanation:
        # There are only three combinations which have a total of 4000, 6000, and 8000 miles, respectively.
        # Since 6000 is the largest use that does not exceed 7000, [2,1] is the optimal pair.

    def test_question_2_where_there_are_more_than_one_optimal_route(self):
        max_travel_distance = 10000

        forwardRouteList = [[1, 3000],
                            [2, 5000],
                            [3, 7000],
                            [4, 10000]]

        returnRouteList = [[1, 2000],
                           [2, 3000],
                           [3, 4000],
                           [4, 5000]]

        output = [[2, 4], [3, 2]]

        self.assertCountEqual(src.question_2.optimalUtilization(max_travel_distance, forwardRouteList, returnRouteList),
                              output)
        ## Explanation
        # There are two pairs of forward and return shipping routes possible that optimally utilizes
        # the given aircraft.
        # Shipping route ID #2 from the forward shipping route list requires 5000 miles travelled, and shipping route ID # 4 from the return shipping route list also requires 5000 miles travelled -- combined, they add up to 10000 miles travelled.
        #
        # Similarly, shipping route #3 from the forward shipping routes list requires 7000 miles travelled, and shipping route ID #2 from return shipping route list requires
        # 3000 miles travelled. These also add up to 10000 miles travelled.
        # Therefore, the pairs of forward and return routes that optimally utilize the aircraft
        # are [2,4] and [3,2].
