""" https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
632. Smallest Range Covering Elements from K Lists  Hard

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:
    Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    Output: [20,24]
    Explanation:
        List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
        List 2: [0, 9, 12, 20], 20 is in range [20,24].
        List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:
    Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
    Output: [1,1]

Example 3:
    Input: nums = [[10,10],[11,11]]
    Output: [10,11]

Example 4:
    Input: nums = [[10],[11]]
    Output: [10,11]

Example 5:
    Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
    Output: [1,7]


Constraints:
  nums.length == k
  1 <= k <= 3500
  1 <= nums[i].length <= 50
  -105 <= nums[i][j] <= 105
  nums[i] is sorted in non-decreasing order.

"""

from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Intuition:  We have to visit every number in each list.

        time: O(n)
        space: O(n)

        Walkthrough:
        1. Starting at index 0 (j), calculate the minimum and maximum of nums[i][j].
        2. If != last index, increment the index of the minimum value
        3. Get min and max of each value
        4. If the val of the current range is less than previous, update the min/max.
        4. return [min, max]

        [4,10,15,24,26]         [0, 0, 0, 0, 0]
                    ^
        [0,9,12,20]             [-1, 0, 0, 0, 0]
                 ^
        [5,18,22,30]            [1, 0, 0, 0, 0]
                  ^

        range [0,5] -> 6        <- min
        range [4-9] -> 6
        range [5-10] -> 6
        range [9-18] -> 10
        range [10-18] -> 9
        range [12-18] -> 6
        range [15-20] -> 6
        range [18-24] -> 7
        range [20-24] -> 5      <- min
        range [20-30] -> 11

        """
        pass

if __name__ == '__main__':
    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    solution = Solution().smallestRange(nums)
    print(solution)
