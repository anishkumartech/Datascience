class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop an element.")

    def isEmpty(self):
        return len(self.stack) == 0



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.isEmpty())  # Output: False
print(stack.pop())  # Output: 20
print(stack.pop())  # Output: 10
print(stack.isEmpty())  # Output: True
