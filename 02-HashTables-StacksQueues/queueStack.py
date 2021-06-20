""" https://leetcode.com/problems/implement-queue-using-stacks/
232. Implement Queue using Stacks   Easy

06/20/2021 15:43	Accepted

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
  - You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
  - Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

Example 1:
  Input:  ["MyQueue", "push", "push", "peek", "pop", "empty"]
          [[], [1], [2], [], [], []]
  Output: [null, null, null, 1, 1, false]
  Explanation:
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false

Constraints:
  1 <= x <= 9
  At most 100 calls will be made to push, pop, peek, and empty.
  All the calls to pop and peek are valid.
"""

# class MyQueue:
#     """
#     this implements a queue, does not comply with stack LIFO properties
#     """
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = []

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         self.queue.append(x)

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         return self.queue.pop(0)

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         return self.queue[0] if not self.empty() else None

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return True if not self.queue else False

class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, val):
        self.stack.append(val)
        self.len += 1

    def pop(self):
        if not self.isEmpty():
            self.len -= 1
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1] if not self.isEmpty() else None

    def isEmpty(self):
        return self.len == 0

    def __repr__(self):
        return str(self.stack)

class MyQueue:
    """
    Why 2 stacks?
    - Stack is LIFO (last in - first out) data structure.
    - To satisfy FIFO property of a queue, need to keep two stacks.

    - Stack 1: store reverse arrival order
    - Stack 2: store queue elements in their final order
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while not self.stack_out.isEmpty():
            self.stack_in.push(self.stack_out.pop())
        self.stack_in.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while not self.stack_in.isEmpty():
            self.stack_out.push(self.stack_in.pop())
            # print(f'POP: {self}')
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        while not self.stack_in.isEmpty():
            self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack_in.isEmpty() and self.stack_out.isEmpty()

    def __repr__(self):
        # return f'{self.stack_in or sorted(self.stack_out, reverse=True)}'
        return f'In: {self.stack_in}\nOut: {self.stack_out}'

# Your MyQueue object will be instantiated and called as such:

# obj = MyQueue()
# obj.push(3)
# param_2 = obj.pop()
# print(param_2)

# param_3 = obj.peek()
# print(param_3)

# param_4 = obj.empty()
# print(param_4)
cmd = ["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
val = [[],[1],[2],[3],[4],[],[5],[],[],[],[]]

for i in range(len(cmd)):
    if cmd[i] == "MyQueue":
        queue = MyQueue()
    elif cmd[i] == "push":
        queue.push(val[i])
    elif cmd[i] == "pop":
        print(queue.pop())

    print(queue)
