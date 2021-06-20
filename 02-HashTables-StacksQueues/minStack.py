""" https://leetcode.com/problems/min-stack/
155. Min Stack  Easy

06/20/2021 14:13	Accepted

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
  MinStack() initializes the stack object.
  void push(val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.

Evalample 1:
    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Evalplanation
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2

Constraints:
    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, val: int) -> None:
        if self.min is None or self.min > val:
            self.min = val
        self.stack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if val <= self.min:
            self.min = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

    def __repr__(self):
        return str([val for val in self.stack] or None)

if __name__ == '__main__':

    minStack = MinStack()

    for i in range(10):
        minStack.push(i)
        print(minStack)
        print(minStack.getMin())

    # minStack.push(-2)
    # minStack.push(0)
    # minStack.push(-3)
    # minStack.push(5)
    # minStack.push(-8)
    # print(f'Minstack {minStack}')
    # print(f'min: {minStack.getMin()}')
    # print(f'top: {minStack.top()}')

    # minStack.pop()

    # print(f'Minstack {minStack}')
    # print(f'min: {minStack.getMin()}')

    # print(f'Minstack {minStack}')
    # print(f'top: {minStack.top()}')
    # print(f'min: {minStack.getMin()}')

    # minStack.pop()

    # print(f'Minstack {minStack}')
    # print(f'top: {minStack.top()}')
    # print(f'min: {minStack.getMin()}')

    # minStack.pop()
    # print(f'Minstack {minStack}')
    # print(f'top: {minStack.top()}')
    # print(f'min: {minStack.getMin()}')
