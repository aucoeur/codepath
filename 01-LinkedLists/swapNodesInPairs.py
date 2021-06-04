""" https://leetcode.com/problems/swap-nodes-in-pairs/
24. Swap Nodes in Pairs     Medium

06/03/2021 17:36	Accepted    Iterative
06/03/2021 14:44	Accepted    Recursive

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
  Input: head = [1,2,3,4]
  Output: [2,1,4,3]

Example 2:
  Input: head = []
  Output: []

Example 3:
  Input: head = [1]
  Output: [1]

Constraints:
  The number of nodes in the list is in the range [0, 100].
  0 <= Node.val <= 100
"""

from typing import List
from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         """
#         Recursive
#         """
#         # Base Cases
#         if not head or not head.next:
#             return head

#         nextOdd = head.next.next

#         # swap
#         head, head.next = head.next, head
#         head.next.next = self.swapPairs(nextOdd)

#         return head

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        Iterative Solution
        """
        if not head:
            return head

        dummy = previous = ListNode(0)
        dummy.next = current = head

        while current and current.next:
            # placeholders
            first = current
            second = current.next

            previous.next = second # update link from previous.next -> second of the pair
            first.next = second.next # this will be the first of the next pair
            second.next = first # now that second.next node is relinked, we can swap/reassign the former second.next pointer to first

            # incrementing previous and current pointers for traversing
            previous, current = first, first.next

        return dummy.next

if __name__ == '__main__':
    head = [1,2,3,4,5,6]
    h = generateLinkedList(head)
    displayLinkedList(h)
    solution = Solution().swapPairs(h)
    displayLinkedList(solution)
