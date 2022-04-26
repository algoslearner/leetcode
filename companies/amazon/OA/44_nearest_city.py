# https://leetcode.com/discuss/interview-question/949904/Amazon-or-OA2-or-Nearest-City
'''
Given a list of points, find the nearest points that shares either an x or a y coordinate with the queried point.

The distance is denoted on a Euclidean plane: the difference in x plus the difference in y.

Input

numOfPoints, an integer representing the number of points;

points, a list of strings representing the names of each point [i];

xCoordinates, a list of integers representing the X coordinates of each point[i];

yCoordinates, a list of integers representing the Y coordinates of each point[i];

numOfQueriedPoints, an integer representing the number of points queried;

queriedPoints, a list of strings representing the names of the queried points.

Output

Return a list of strings representing the name of the nearest points that shares either an x or a y coordinate with the queried point.

Example 1:

Input:

numOfPoints = 3

points = ["p1","p2","p3"]

xCoordinates = [30, 20, 10]

yCoordinates = [30, 20, 30]

numOfQueriedPoints = 3

queriedPoints = ["p3", "p2", "p1"]

Output:

["p1", NONE, "p3"]

Example 2:

Input:

numOfPoints = 5

points = ["p1", "p2","p3", "p4", "p5"]

xCoordinates = [10, 20, 30, 40, 50]

yCoordinates = [10, 20, 30, 40, 50]

numOfQueriedPoints = 5

queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

Output

[NONE, NONE, NONE, NONE, NONE]
'''


###############################################################################################
# shameless brute force solution:

def nearestCity(points, xCoordinates, yCoordinates, Q):
    P = {}
    x_P = {}
    y_P = {}

    S = []
    for p, x, y in zip(points, xCoordinates, yCoordinates):
        P[p] = (x, y)
        if x not in x_P:
            x_P[x] = []
        if y not in y_P:
            y_P[y] = []

        x_P[x].append(p)
        y_P[y].append(p)

    for q in Q:
        qx, qy = P[q]
        xpoints = []
        ypoints = []
        if qx in x_P:
            xpoints = list(x_P[qx])
            xpoints.remove(q)
        if qy in y_P:
            ypoints = list(y_P[qy])
            ypoints.remove(q)
        if xpoints:
            # can do binary search here to get O(nlogn) solution.. but who gives a s**t, stupid question
            S.append(sorted([(p, P[p]) for p in xpoints], key=lambda x: abs(qy - x[1][1]))[0][0])
        elif ypoints:
            S.append(sorted([(p, P[p]) for p in ypoints], key=lambda x: abs(qx - x[1][0]))[0][0])
        else:
            S.append("NONE")

    return S
  
  ################################################################################################
  # SOLUTION 2
#
Python with sorting and binary search

from collections import defaultdict

class NearestCities:
    def binary_search(self, p_id, l, axis=1):  # axis 0 for x and 1 for y
        left, right = 0, len(l) - 1

        while left <= right:
            mid = left + (right-left)//2
            p_m = l[mid]
            if l[mid] == p_id:
                return mid
            elif self.points[p_m][axis] > self.points[p_id][axis]:
                right = mid - 1
            else:
                left = mid + 1

    def is_closest_point(self, p_id, k, l, closest_point, axis=1):
        if 0 <= k < len(l):
            p1 = l[k]
            print(p_id, p1)
            if abs(self.points[p1][axis] - self.points[p_id][axis]) < closest_point[1]:
                closest_point = [p1, abs(self.points[p1][axis] - self.points[p_id][axis]) ]

        return closest_point

    def set_close_point(self, p_id, i, j, x_points, y_points, result ):
            closest_point = [ None,  float('inf') ]
            # x left and right
            closest_point = self.is_closest_point(
                p_id, i-1, x_points,closest_point, axis=1)
            closest_point = self.is_closest_point(
                p_id, i+1, x_points,closest_point, axis=1)

            # y top and left
            closest_point = self.is_closest_point(
                p_id, j-1, y_points, closest_point, axis=0)
            closest_point = self.is_closest_point(
                p_id, j+1, y_points, closest_point, axis=0)

            print(p_id, closest_point)
            result.append(closest_point[0])

    def nearest_cities(self, pins, x_coordinates, y_coordinates, target_pins):
        self.points = defaultdict()
        x_pins = defaultdict(list)
        y_pins = defaultdict(list)

        result = []

        for p_id, x, y in zip(pins, x_coordinates, y_coordinates):
            self.points[p_id] = (x, y)
            x_pins[x].append(p_id)
            y_pins[y].append(p_id)

        for _, items in x_pins.items():
            items.sort(key=lambda p: self.points[p][1])

        for _, items in y_pins.items():
            items.sort(key=lambda p: self.points[p][0])

        # print(x_pins, y_pins, points)

        for p_id in target_pins:
            x, y = self.points[p_id]
            x_points = x_pins[x]
            y_points = y_pins[y]

            i = self.binary_search(p_id, x_points, axis=1) 
            j = self.binary_search(p_id, y_points, axis=0) 
            #print(i, j, p_id, x_points, y_points)

            self.set_close_point( p_id, i, j, x_points, y_points, result )

        return result


pins = ["a", "b", "c", "d", "e"]
x_coordinates = [50, 60, 100, 200, 300]
y_coordinates = [50, 60, 50, 200, 50]
target_pins = ["a", "b", "c", "d", "e"]
Output = ["c", "NONE", "a", "NONE", "c"]
print(NearestCities().nearest_cities(pins, x_coordinates, y_coordinates, target_pins))
