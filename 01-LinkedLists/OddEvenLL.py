""" https://leetcode.com/problems/odd-even-linked-list/
328. Odd Even Linked List   Easy

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.


Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]


Constraints:
  The number of nodes in the linked list is in the range [0, 104].
  -106 <= Node.val <= 106

Follow up: Could you solve it in O(1) space complexity and O(nodes) time complexity?
"""
from ..utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return ListNode

head = [2,1,3,5,6,4,7]
solution = Solution().oddEvenList(head)
print(solution)
