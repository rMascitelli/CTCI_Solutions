# Stack implemented using a LinkedList
from linked_list import *

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        # Create new Node to add
        temp = Node(val)

        # If the Stack is empty, top = new Node
        if(self.top == None):
            self.top = temp
        # Else, Set next to the current top, and replace current top with temp
        else:
            self.top.next = self.top
            self.top = temp 

    def printall(self):
        # Empty Stack
        if(self.top == None):
            print("None")
            return
        else:
            print(self.top.value)
            temp = self.top.next
            while(temp != None):
                temp = temp.next
                print(temp)
            

stk = Stack()
stk.push(5)
stk.push(4)
stk.push(3)
stk.printall()
