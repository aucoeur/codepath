""" https://leetcode.com/problems/linked-list-cycle-ii/
142. Linked List Cycle II   Medium

06/03/2021 13:07	Accepted

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Constraints:
  The number of the nodes in the list is in the range [0, 104].
  -105 <= Node.val <= 105
  pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from utilities import ListNode, generateLinkedList, displayLinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        First: Detect Cycle - Two pointer, fast, slow, look for intersection
        Then: Find Start of Cycle - Start one pointer from head, increment both 1 step at a time until they meet

        NOTE: can't just return slow or fast after cycle detected
            because that is just where they both meet/intersect,
            whereas this problem is asking for where the loop begins
        """

        # Base Case: Empty or 1 node
        if not head or not head.next:
            return None

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # print(f'Slow: {slow} -> {slow.next}\nFast: {fast} -> {fast.next}\n')

            # if fast == slow:
                # return slow # <- NO. this only returns the meeting point

            # find start of cycle:
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

if __name__ == "__main__":
    boop = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
    # print(len(boop), boop[24]) # 5 -> 21

    # make nodes from array
    boopNodes = []
    for item in boop:
        boopNodes.append(ListNode(item))

    head = boopNodes[0]
    # add node.next
    for node in boopNodes[1:]:
        head.next = node
        head = head.next

    # add tail cycle
    boopNodes[-1].next = boopNodes[24]

    # print(boopNodes[-1], boopNodes[-1].next)

    # displayLinkedList(boopNodes[0])
    solution = Solution().detectCycle(boopNodes[0])
    for i in range(len(boopNodes)):
        if solution == boopNodes[i]:
            print(i)
    print(solution)




    head = [3,2,0,-4]

    h1 = ListNode(head[0])
    h2 = ListNode(head[1])
    # h3 = ListNode(head[2])
    # h4 = ListNode(head[3])

    h1.next = h2
    h2.next = h1 # cycle
    # h2.next = h3
    # h3.next = h4
    # h4.next = h2

    # node = h1
    # for i in range(6):
    #     print(node)
    #     node = node.next

    solution2 = Solution().detectCycle(h1)
    print(solution2)
