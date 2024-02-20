# A class to represent a singly linked list.
class SLList:
    
    # Nested class to represent a node in the linked list.
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item  # Value contained in the node.
            self.next = next_node  # Reference to the next node in the list.
            
    def __init__(self):
        self.first = None  # Initialize an empty linked list.

    # Add an element at the beginning of the list.
    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    # Insert an element at a specific position in the list.
    def insert(self, item, position):
        # If list is empty or position is at the beginning, add the item at the front.
        if self.first is None or position <= 0:
            self.addFirst(item)
            return
        
        # Traverse the list to find the right position.
        current = self.first
        for i in range(1, position):
            if current.next is None:  # If reached end of the list, break.
                break
            current = current.next
        
        # Insert the new node after the current node.
        new_node = self.IntNode(item, current.next)
        current.next = new_node

    # Reverse the linked list.
    def reverse(self):
        prev = None
        current = self.first
        
        # Traverse the list and reverse the pointers.
        while current is not None:
            next_node = current.next  # Keep a reference to the next node.
            current.next = prev
            prev = current
            current = next_node
        
        self.first = prev  # Set the head to the last node.

    # Create a new list where each item is replicated by its value.
    def replicate(self):
        replicated_head = self.IntNode(0, None)  # Dummy node to ease operations.
        current_replicated = replicated_head

        current_original = self.first
        while current_original:
            for _ in range(current_original.item):  # Replicate the current item.
                new_node = self.IntNode(current_original.item, None)
                current_replicated.next = new_node
                current_replicated = current_replicated.next

            current_original = current_original.next  # Move to the next node.

        return replicated_head.next  # Return the head of the replicated list, skipping the dummy node.

    # Return a string representation of the list.
    def __str__(self):
        items = []
        current = self.first
        while current:
            items.append(str(current.item))
            current = current.next
        return '->'.join(items)
    
    # Check if two lists are equal.
    def equals(self, anotherList):
        current1 = self.first
        current2 = anotherList.first
        
        while current1 is not None and current2 is not None:
            if current1.item != current2.item:
                return False
            current1 = current1.next
            current2 = current2.next
        
        return current1 is None and current2 is None

# Begin testing.
print("Testing below \n \n")

# Create and populate a list.
list1 = SLList()
list1.addFirst(3)
list1.addFirst(2)
list1.addFirst(1)
print("Original List: ", list1, "\n") 

# Test the insert method.
list1.insert(4,3)
print("1.1) Insert Method add a 4 to end of list: ", list1) 

# Test the reverse method.
list1.reverse()
print("1.2) Reverse List Method Test:", list1)

# Test the replicate method.
list1.first = list1.replicate() 
print("1.3) Replicate Method Test:", list1)

# Test the equals method.
L = SLList()
L.addFirst(15)
L.addFirst(10)
L.addFirst(5)
L.reverse()

L_expect = SLList()
L_expect.addFirst(5)
L_expect.addFirst(10)
L_expect.addFirst(15)	

# Check if two lists are the same.
if L.equals(L_expect):
    print("1.4) Two lists are equal, tests passed")
else:
    print("1.4) Two lists are not equal, tests failed")









