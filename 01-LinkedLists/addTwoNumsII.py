""" https://leetcode.com/problems/add-two-numbers-ii/
445. Add Two Numbers II     Medium

06/06/2021 09:26	Accepted

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]


Constraints:
  - The number of nodes in each linked list is in the range [1, 100].
  - `0 <= Node.val <= 9`
  - It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
"""
from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Sum of each linkedList individually, then create new list from adding both sums together
        """

        sum_l1 = sum_l2 = 0

        while l1:
            # each pass we multiply existing val * 10 to increase digit place
            sum_l1 = (sum_l1 * 10) + l1.val
            l1 = l1.next

        while l2:
            sum_l2 = (sum_l2 * 10) + l2.val
            l2 = l2.next

        total = str(sum_l1 + sum_l2) # convert to string to prep for making LL
        dummy = ListNode(0)

        dummy.next = head = ListNode(int(total[0]))
        for i in range(1, len(total)):
            head.next = ListNode(int(total[i]))
            head = head.next
        return dummy.next

if __name__ == '__main__':
    # l1 = generateLinkedList([7,2,4,3])
    # l2 = generateLinkedList([5,6,4])
    # Output [7,8,0,7]

    l1 = generateLinkedList([0])
    l2 = generateLinkedList([0])
    # Output [0]
    solution = Solution().addTwoNumbers(l1, l2)
    displayLinkedList(solution)
