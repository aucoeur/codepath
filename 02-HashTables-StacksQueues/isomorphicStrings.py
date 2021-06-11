""" https://leetcode.com/problems/isomorphic-strings/description/
205. Isomorphic Strings     Easy

06/06/2021 20:56	Accepted

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
  1 <= s.length <= 5 * 104
  t.length == s.length
  s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Base Case: len not same
        if len(s) != len(t):
            return False
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                if t[i] != seen[s[i]]:
                    return False
            else:
                if t[i] in seen.values():
                    return False
                seen[s[i]] = t[i]
        return True


if __name__ == '__main__':
    s = "foo"
    # t = "add"
    t= 'bar'
    solution = Solution().isIsomorphic(s,t)
    print(solution)
