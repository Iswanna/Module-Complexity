class Node:
    """
    Represents a single person in line.
    Stores a value and links to the people ahead and behind.
    """
    __slots__ = ['value', 'next', 'previous']

    def __init__(self, value):
        self.value = value
        self.next = None      
        self.previous = None  


class LinkedList:
    """
    Manages the line by keeping track of the Head and the Tail.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        """Adds a new node to the front of the list."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
      
        else:
            new_node.next = self.head      
            self.head.previous = new_node  
            self.head = new_node          
        
        return new_node

    def pop_tail(self):
        """Removes the last node and returns its value."""
      
        if self.tail is None:
            return None

        value_to_return = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
    
        else:
            self.tail = self.tail.previous  # Move tail back one
            self.tail.next = None           # New tail lets go of the old tail

        return value_to_return

    def remove(self, node):
        """Removes a specific node from anywhere in the list."""
        if node is None:
            return

        if node == self.head:
            self.head = node.next
        
        if node == self.tail:
            self.tail = node.previous

        if node.previous is not None:
            node.previous.next = node.next
            
        if node.next is not None:
            node.next.previous = node.previous

        node.next = None
        node.previous = None