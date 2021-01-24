import unittest
import stack


class TestStack(unittest.TestCase):

    def test_top(self):
        myStack = stack.Stack()
        myStack.add("Mon")
        myStack.add("Tue")
        myStack.add("Wed")
        myStack.add("Thur")

        self.assertEquals(myStack.top(), "Thur")

        self.assertEquals(myStack.remove(), "Thur")
        self.assertEquals(myStack.remove(), "Wed")