class Node:
    """
    Step 1: Updated Node class.
    Each node stores both key and value so we can find the 
    dictionary entry when a node is evicted from the tail.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    """
    A Doubly Linked List to track the order of usage.
    Head is Most Recently Used (MRU).
    Tail is Least Recently Used (LRU).
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, node):
        """Adds an existing node to the front of the list."""
        node.next = self.head
        node.previous = None
        
        if self.head is not None:
            self.head.previous = node
        
        self.head = node
        
        # If list was empty, this node is also the tail
        if self.tail is None:
            self.tail = node

    def pop_tail(self):
        """Removes the last node (the oldest item) and returns it."""
        if self.tail is None:
            return None

        old_tail = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            
        return old_tail
