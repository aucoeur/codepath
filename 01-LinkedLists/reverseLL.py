""" https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List    Easy

05/28/2021 23:38	Accepted

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
  The number of nodes in the list is the range [0, 5000].
  -5000 <= Node.val <= 5000
"""
from linkedlist import ListNode, generateLinkedList, displayLinkedList

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        previous = None

        while current:
            placeholder = current.next
            current.next = previous

            previous = current
            current = placeholder
        return previous


head = [1,2,3,4,5]
linkedlist = generateLinkedList(head)
solution = Solution().reverseList(linkedlist)
displayLinkedList(solution)
