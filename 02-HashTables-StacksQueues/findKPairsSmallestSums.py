""" https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
373. Find K Pairs with Smallest Sums    Medium

06/19/2021 13:17	Accepted

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


Example 1:
  Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
  Output: [[1,2],[1,4],[1,6]]
  Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
  Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
  Output: [[1,1],[1,1]]
  Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
  Input: nums1 = [1,2], nums2 = [3], k = 3
  Output: [[1,3],[2,3]]
  Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:
  1 <= nums1.length, nums2.length <= 104
  -109 <= nums1[i], nums2[i] <= 109
  nums1 and nums2 both are sorted in ascending order.
"""

from typing import List
from heapq import heappush, heapreplace, nsmallest

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        kSmallSums = []

        for pointer in range(len(nums1)):
            for pointer2 in range(len(nums2)):

                currentSum = nums1[pointer] + nums2[pointer2]

                # heap only holds maxMin len(k)
                if len(kSmallSums) < k:
                    # negative priority to comply with maxHeap
                    heappush(kSmallSums, (-currentSum, [nums1[pointer], nums2[pointer2]]))
                # peek at top of maxHeap
                elif currentSum < -kSmallSums[0][0]:
                    heapreplace(kSmallSums, (-currentSum, [nums1[pointer], nums2[pointer2]]))
                # since sorted, break early if larger sum
                else:
                    # print(nums1[pointer],nums2[pointer2])
                    break

        return [x[1] for x in kSmallSums]


if __name__ == '__main__':
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    solution = Solution().kSmallestPairs(nums1, nums2, k)
    print(solution)
