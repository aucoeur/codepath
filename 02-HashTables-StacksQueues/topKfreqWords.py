""" https://leetcode.com/problems/top-k-frequent-words/description/
692. Top K Frequent Words   Medium

06/17/2021 13:28	Accepted

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up: Try to solve it in O(n log k) time and O(n) extra space
"""

from typing import List
from heapq import heapify, heapreplace, heappush, nlargest, nsmallest

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Time: O(n + k log n)
        Space: O(n)
        """
        histo = {}

        # O(n)
        for word in words:
            histo[word] = histo.get(word, 0) + 1

        # O(n) - use negative value because min heap
        # topK = [(-v, k) for k,v in histo.items()]
        # heapify(topK) # O(n) since heapify entire list instead of pushing one by one

        # O(k log n) use min heap & nsmallest because we need to return alphabetical order in event of same count/priority
        # return [item[1] for item in nsmallest(k, topK)]

        # one liner of lines 43-48
        return nsmallest(k, histo.keys(), key=lambda word: (-histo[word], word))

if __name__ == '__main__':
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    # words = ["i", "love", "leetcode", "i", "love", "coding"]
    # k = 2
    solution = Solution().topKFrequent(words, k)
    print(solution)
