""" https://leetcode.com/problems/k-closest-points-to-origin/
973. K Closest Points to Origin     Medium

06/19/2021 14:59	Accepted

Given an array of points where points[i] = [x_i, y_i] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x_1 - x_2)^2 + (y_1 - y_2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Example 1:
  Input: points = [[1,3],[-2,2]], k = 1
  Output: [[-2,2]]
  Explanation:
   - The distance between (1, 3) and the origin is sqrt(10).
   - The distance between (-2, 2) and the origin is sqrt(8).
   - Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
   - We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
  Input: points = [[3,3],[5,-1],[-2,4]], k = 2
  Output: [[3,3],[-2,4]]
  Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:
  1 <= k <= points.length <= 104
  -104 < x_i, y_i < 104
"""

from typing import List
from math import sqrt
from heapq import heapify, heappush, nsmallest

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

#         x2, y2 = 0, 0 # origin
#         distances = []

#         for point in points:
#             x1, y1 = point[0], point[1]
#             # Euclidean Distance: √(x_1 - x_2)^2 + (y_1 - y_2)^2)
#             eucDistance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
#             distances.append((eucDistance, point))

#         heapify(distances)

#         return [x[1] for x in nsmallest(k, distances)]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Intuition:
        can just skip the sqrt, since we know anything greater will sqrt into a larger value anyway
        """

        # use sorted to avoid modifying original list
        # key will sort by val of pre-sqrt of distances (no x_2, y_2 because origin is 0,0)
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:k]



if __name__ == '__main__':
    # points = [[3,3],[5,-1],[-2,4]]
    points = [[1,3],[-2,2]]
    k = 1
    solution = Solution().kClosest(points, k)
    print(solution)
