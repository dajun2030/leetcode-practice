class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# 测试示例
if __name__ == "__main__":
    # 测试用例1
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"getMin: {minStack.getMin()}")  # 返回 -3
    minStack.pop()
    print(f"top: {minStack.top()}")  # 返回 0
    print(f"getMin: {minStack.getMin()}")  # 返回 -2
    print()

    # 测试用例2
    minStack2 = MinStack()
    minStack2.push(5)
    minStack2.push(2)
    minStack2.push(8)
    minStack2.push(1)
    print(f"getMin: {minStack2.getMin()}")  # 返回 1
    minStack2.pop()
    print(f"getMin: {minStack2.getMin()}")  # 返回 2
    minStack2.pop()
    print(f"top: {minStack2.top()}")  # 返回 2
    print(f"getMin: {minStack2.getMin()}")  # 返回 2