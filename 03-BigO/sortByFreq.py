""" https://leetcode.com/problems/sort-characters-by-frequency/description/
451. Sort Characters By Frequency - Medium

08/11/2021 17:21	Accepted    https://leetcode.com/submissions/detail/537086251/

Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

Example 1:
  Input: s = "tree"
  Output: "eert"
  Explanation: 'e' appears twice while 'r' and 't' both appear once.
  So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
  Input: s = "cccaaa"
  Output: "aaaccc"
  Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
  Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
  Input: s = "Aabb"
  Output: "bbAa"
  Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
  Note that 'A' and 'a' are treated as two different characters.

Constraints:
  1 <= s.length <= 5 * 105
  s consists of English letters and digits.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        """
        time complexity: O(n)
          - O(n) to build the histo
          - O(n) to sort the histo
          - O(n) to join the list comprehension
        space complexity: O(n)
        """
        # create a histogram to count the frequency of each character
        histogram = {}

        for char in s:
            histogram[char] = histogram.get(char, 0) + 1

        # sort the histogram in descending order
        sorted_histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

        return "".join([k * v for k, v in sorted_histogram])

if __name__ == '__main__':
    # s = "Aabb"
    s = "cccaaa"
    solution = Solution().frequencySort(s)
    print(solution)
