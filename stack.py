class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return ("no elements left")
        else:
            return self.stack.pop()

    def top(self):
        if len(self.stack) <= 0:
            return ("Stack is empty")
        else:
            return self.stack[-1]


AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thur")
print("Top: " + AStack.top())
print(AStack.remove())
print(AStack.remove())
