# We can use a Singly Linked List as a stack

# Insert into a stack (push) is the same as Adding to the front of a SLL

# Removing from a stack (pop) is the same as Removing from the front of a SLL

# The goal is to use what we know about SLL to build a Stack with the following methods
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # challenge for you guys
    def Push(self, val):
        #This code should handle pushing into a stack
        pass

    def Pop(self):
        # This code should handle removing from a stack
        pass

    def Peek(self):
        # This code should handle showing what is at the top of a stack
        pass
