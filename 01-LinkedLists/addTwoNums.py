""" https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers  Medium

05/29/2021 20:23	Accepted  https://leetcode.com/submissions/detail/500167319/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
  The number of nodes in each linked list is in the range [1, 100].
  0 <= Node.val <= 9
  It is guaranteed that the list represents a number that does not have leading zeros.
"""
from utilities import ListNode, generateLinkedList, displayLinkedList

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        currentSum = carry = 0

        head = ListNode() # dummy head
        node = head

        while l1 or l2 or carry:
            num1 = l1.val if l1 else head.val
            num2 = l2.val if l2 else head.val

            currentSum = (num1 + num2) + carry

            if carry == 1:
                carry = 0 # reset carry

            if currentSum >= 10:
                carry = 1 # carry the one

            newNode = ListNode(currentSum % 10) # create node with single digit val

            node.next = newNode
            node = newNode # increment node, l1 and l2

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # return linkedlist after dummy head
        return head.next

list1 = [2,4,3]
list2 = [5,6,4]
# Output: [7,0,8]
# list1 = [9,9,9,9,9,9,9]
# list2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
l1 = generateLinkedList(list1)
l2 = generateLinkedList(list2)
displayLinkedList(l1)
displayLinkedList(l2)

solution = Solution().addTwoNumbers(l1, l2)
displayLinkedList(solution)

"""
Cleaned up Solution
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = current = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)
            current = current.next
            carry = carry // 10 # int division, will return 0 or 1
        return dummy.next
