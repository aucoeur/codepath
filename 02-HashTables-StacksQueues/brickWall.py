""" https://leetcode.com/problems/brick-wall/

08/08/2021 Accepted https://leetcode.com/submissions/detail/535513182/

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:
  Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
  Output: 2

Example 2:
  Input: wall = [[1],[1],[1]]
  Output: 3

Constraints:
  n == wall.length
  1 <= n <= 104
  1 <= wall[i].length <= 104
  1 <= sum(wall[i].length) <= 2 * 104
  sum(wall[i]) is the same for each row i.
  1 <= wall[i][j] <= 231 - 1
"""
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        using the first row as a reference, count number of bricks with the width > first row width by column
        [
            [1,2,2,1],
            [3,1,2],
            [1,3,2],
            [2,4],
            [3,1,2],
            [1,3,1,1]
        ]
        """

        height = len(wall)
        width = sum(wall[0])
        counts = {}

        print(f'Height: {height}\nWidth: {width}')

        for row in wall:
            print(f'\nRow: {row}')
            brickend = 0
            for brick in row:
                print(f'Brick: {brick}')
                brickend += brick
                # key is the brick end edge,
                # value is height minus brickends seen so far
                counts[brickend] = counts.get(brickend, height) - 1

                # dict comprehension to print count dict sorted by keys
                print(f'{dict(sorted(counts.items()))}')

        # drops last edge
        counts[width] = height

        return min(counts.values())



if __name__ == '__main__':
    # wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1],[1,1,1,1,1,1]]
    # wall = [[1],[1],[1]]
    # wall = [[2],[2],[2]]
    wall = [[6],[6],[2,4],[6],[1,2,2,1],[6],[2,1,2,1],[1,5],[4,1,1],[1,4,1],[4,2],[3,3],[2,2,2],[5,1],[5,1],[6],[4,2],[1,5],[2,3,1],[4,2],[1,1,4],[1,3,1,1],[2,3,1],[3,3],[3,1,1,1],[3,2,1],[6],[3,2,1],[1,5],[1,4,1]] # 17
    solution = Solution().leastBricks(wall)
    print(solution)

    solution = Solution().leastBricks(wall)
    print(solution)
