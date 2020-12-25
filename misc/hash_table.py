from linked_list import *

# A HashTable implemented using LinkedList
class HashTable:
    def __init__(self, size):
        # Do I need anything here? Should have to declare members
        self.table = []
        self.size = size
        for i in range(0, self.size):
            self.table.append(LinkedList(None))

    def store(self, val):
        # First find the hash index
        idx = int(val) % self.size

        # Return value based on empty LL or not
        if(self.table[idx] == None):
            self.table[idx] = LinkedList(val)
            return False
        
        else:
            self.table[idx].add(val)
            return True
        
    def printall(self):
        for i in range(0, self.size):
            self.table[i].printall()


test_hash = HashTable(10)
for i in range(0, 100):
    test_hash.store(i)

#test_hash.printall()



