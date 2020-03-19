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
        newnode = SLNode(val)
        newnode.next = self.head
        self.head = newnode
        return self

    def Pop(self):
        if self.head == None:
            print("Stack is empty")
        
        toReturn = self.head
        self.head = toReturn.next
        return toReturn

    def Peek(self):
        if self.head == None:
            print("Stack is empty")
            return self.head
        else:
            # print(self.head.value)
            return self.head.value
