# Try to create a Linked List class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList only needs a member of type "Node"
class LinkedList:
    def __init__(self, value):
        if(type(value) != Node):
            #print("Node not provided! Creating node for LL root")
            tmp_node = Node(value)
            self.head = tmp_node
        else:
            #print("Node provided! Adding node as LL root")
            self.head = value

    def add(self, val):
        if(self.head.value == None):
            self.head.value = val
            return 1                    # Return 1 to tell user the LL was empty
        else:
            # Use temp_node to find a reference to a Node where nxt = None
            temp_node = self.head
            while(temp_node.next != None):
                temp_node = temp_node.next

            # Append new Node to LL, using provided val
            temp_node.next = Node(val)

    def printall(self):
        temp_node = self.head
        print("[" + str(temp_node.value) + "] -> ", end = '')
        while(temp_node.next != None):
            temp_node = temp_node.next
            print("(" + str(temp_node.value) + ") -> ", end = '')
        print("End")

    # O(2n) where n is the length of the LL
    def reverseList(self):
        # First, loop through LL and put every node in an array
        arr = []
        temp = self.head
        while(temp.next != None):
            arr.append(temp)
            temp = temp.next
        arr.append(temp)

        # Now, starting from the last index in arr, form the LL backwards
        ret = LinkedList(None)
        for i in range(len(arr), 0, -1):
            ret.add(arr[i-1].value)

        return ret
'''
a = Node(1)
b = Node(2)
c = Node(3)
ll = LinkedList(a)
ll.add(2)
ll.add(3)
ll.add(4)
ll.printall()
new = ll.reverseList()
new.printall()
'''
