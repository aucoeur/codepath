""" https://leetcode.com/problems/linked-list-cycle
141. Linked List Cycle

05/29/2021 16:31	Accepted

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
    head = [3,2,0,-4], pos = 1
    # Output: true
    # Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
  The number of the nodes in the list is in the range [0, 104].
  -105 <= Node.val <= 105
  pos is -1 or a valid index in the linked-list.

"""
from ..utilities import ListNode

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Intuition: If linkedlist has a cycle, the two pointers will eventually cross paths (fast pointer will lap the slow one)
        """
        # if head or head.next != None, return False
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        # while fast or fast.next != None
        while fast and fast.next:
            if slow == fast: # cycle detected
                return True
            slow = slow.next
            fast = fast.next.next # increment 2 because fast
        return False





head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
