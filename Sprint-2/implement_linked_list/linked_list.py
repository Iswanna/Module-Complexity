class Node:
    """
    Represents a single person in line.
    Stores a value and links to the people ahead and behind.
    """
    def __init__(self, value):
        self.value = value
        self.next = None      # The person ahead
        self.previous = None  # The person behind


class LinkedList:
    """
    Manages the line by keeping track of the Head and the Tail.
    """
    def __init__(self):
        self.head = None
        self.tail = None