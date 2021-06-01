""" https://leetcode.com/problems/odd-even-linked-list/
328. Odd Even Linked List   Medium

06/01/2021 10:37	Accepted

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
from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)

        Intuition:
        Since first node is considered odd and odd/even indices alternate, can always know that:
            odd.next ->  even index
            even.next -> odd index
        """

        # Base Case: empty or len(1)
        if not head or not head.next:
            return head

        # since description says first node considered odd
        odd = head
        current = even = head.next # even doesn't change, always points to beginning of even (head.next)
        # current is temporary placeholder for traversing

        while current and current.next:
            odd.next = current.next # update odd pointer to next odd
            odd = odd.next # increment odd

            current.next = odd.next # update even pointer to next even
            current = current.next # increment current node

        odd.next = even # add even tail to odd.next at the end

        return head

head = [2,1,3,5,6,4,7]
# output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4
h = generateLinkedList(head)
displayLinkedList(h)
solution = Solution().oddEvenList(h)
displayLinkedList(solution)
