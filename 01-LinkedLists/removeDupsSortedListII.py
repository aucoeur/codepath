""" https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
82. Remove Duplicates from Sorted List II   Medium

06/06/2021 18:41	Accepted

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
  The number of nodes in the list is in the range [0, 300].
  -100 <= Node.val <= 100
  The list is guaranteed to be sorted in ascending order.
"""
from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         '''
#         This solution only removes the extras and leaves 1 val, not all values that are duplicated
#         '''

#         node = head
#         pointer = head.next

#         if not head or not head.next:
#             return head

#         while node and pointer:
#             if node.val != pointer.val:
#                 node.next = pointer
#                 node = node.next
#             pointer = pointer.next

#         return head

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        iterative solution with dummy.. should probably try this recursively

        1. use a dummy as previous
        2. move current pointer, until current.next is non-dupe
        3. add current.next to dummy(node.next) list
        4. increment current to next to skip dupes

        Time: O(n)
        Space: O(1)
        '''
        dummy = node = ListNode(0)
        current = head

        # Base case: len(head) <= 1
        if not head or not head.next:
            return head

        while current and current.next:
            # if values are not same,
            if current.val != current.next.val:
                # link current to dummy(node.next)
                # increment node
                node.next = current
                node = node.next
            else:
                # if same, increment current until diff val
                while current.next and current.val == current.next.val:
                    current = current.next # fastforward current to new unique val

            node.next = current.next
            current = current.next

        return dummy.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Recursive solution
        """
        # Base case: len(head) <= 1
        if not head or not head.next:
            return head

        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head

        current = head
        while current.next and current.val == current.next.val:
            current = current.next
        return self.deleteDuplicates(current.next)

if __name__ == '__main__':
    # head = generateLinkedList([1,1,1])
    # head = generateLinkedList([1,2,3,3,4,4,5])
    # Output [1,2,5]
    head = generateLinkedList([1,1,1,1,2,3])
    # Output [2,3]
    solution = Solution().deleteDuplicates(head)
    displayLinkedList(solution)
