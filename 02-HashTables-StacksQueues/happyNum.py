""" https://leetcode.com/problems/happy-number/description/
202. Happy Number   Easy

06/17/2021 12:25	Accepted

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    - Those numbers for which this process ends in 1 are happy.
    - Return true if n is a happy number, and false if not.

Example 1:
    Input: n = 19
    Output: true
Explanation:
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

Example 2:
    Input: n = 2
    Output: false

Constraints:
    1 <= n <= 231 - 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Recursive solution
        """

        def addSquares(n, seen = set()):
            sumSquare = 0
            for digit in str(n):
                sumSquare += int(digit)**2

            if sumSquare in seen:
                return False
            elif sumSquare == 1:
                return True
            else:
                seen.add(sumSquare)

            return addSquares(sumSquare, seen)

        return addSquares(n)

    def isHappyIter(self, n: int) -> bool:
        """
        Iterative solution
        """
        seen = set()

        while n != 1:
            n = sum([int(x)**2 for x in str(n)])

            if n in seen:
                return False

            seen.add(n)
        return True


if __name__ == '__main__':
    n = 2
    solution = Solution().isHappy(n)
    print(solution)
