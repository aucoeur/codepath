""" https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists  Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
  Input: l1 = [1,2,4], l2 = [1,3,4]
  Output: [1,1,2,3,4,4]

Example 2:
  Input: l1 = [], l2 = []
  Output: []

Example 3:
  Input: l1 = [], l2 = [0]
  Output: [0]

Constraints:
  The number of nodes in both lists is in the range [0, 50].
  -100 <= Node.val <= 100
  Both l1 and l2 are sorted in non-decreasing order.
"""
from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Dummy Pointer
        - Set pointer.next to smaller value between nodes in list,
        - increment next in that list
        - pointer = pointer.next to traverse through
        """

        dummy = pointer = ListNode(0)

        while l1 and l2:
            # set pointer to smaller val
            # move to next node to evaluate
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            # move pointer up
            pointer = pointer.next

        # if reach end of either lists,
            # attach other list to tail
        pointer.next = l1 or l2

        return dummy.next


if __name__ == '__main__':
    l1 = generateLinkedList([2,4,6])
    l2 = generateLinkedList([1,3,5])
    solution = Solution().mergeTwoLists(l1, l2)
    displayLinkedList(solution)
