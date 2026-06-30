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

   