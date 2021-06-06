""" https://leetcode.com/problems/rotate-list/
61. Rotate List     Medium

06/04/2021 08:38	Accepted

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
  Input: head = [1,2,3,4,5], k = 2
  Output: [4,5,1,2,3]

Example 2:
  Input: head = [0,1,2], k = 4
  Output: [2,0,1]

Constraints:
  The number of nodes in the list is in the range [0, 500].
  -100 <= Node.val <= 100
  0 <= k <= 2 * 109
"""

from collections import deque
from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        Maybe track previous nodes instead of pop and re-insert into the stack
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0, next=head)
        node = head

        stack = deque()

        while node:
            stack.append(node)
            node = node.next

        rotations = k % len(stack)

        for _ in range(rotations):
            tail = stack.pop()
            previous = stack.pop()

            previous.next = None
            tail.next = head
            dummy.next = tail
            head = dummy.next

            stack.append(previous)
            stack.insert(0, tail)

        return dummy.next

if __name__ == '__main__':
    # head, k = [1,2,3,4,5] , 2
    # head, k = [0,1,2], 4
    head = [1,2,3]
    k = 2000000000
    # Output: [4,5,1,2,3]
    h = generateLinkedList(head)
    displayLinkedList(h)

    solution = Solution().rotateRight(h, k)
    displayLinkedList(solution)
