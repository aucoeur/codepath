""" https://leetcode.com/problems/jewels-and-stones/description/
771. Jewels and Stones      Easy

06/10/2021 21:53	Accepted

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
  1 <= jewels.length, stones.length <= 50
  jewels and stones consist of only English letters.
  All the characters of jewels are unique.
"""
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numJewels = 0
        jewelSet = set(jewels)
        for stone in stones:
            if stone in jewelSet:
                numJewels += 1
        return numJewels

if __name__ == '__main__':
    jewels = "z"
    stones = "ZZ"
    solution = Solution().numJewelsInStones(jewels, stones)
    print(solution)
