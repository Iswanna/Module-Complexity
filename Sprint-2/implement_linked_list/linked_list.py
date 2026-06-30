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

    def push_head(self, value):
        """Adds a new node to the front of the list."""
        new_node = Node(value)

        # Logic 2: If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Logic 3: If the list is not empty
        else:
            new_node.next = self.head      # New person grabs old head's hand
            self.head.previous = new_node  # Old head reaches back to new person
            self.head = new_node           # New person is now the head
        
        # Logic 4: Return the node so we can reference it later
        return new_node

    def pop_tail(self):
        """Removes the last node and returns its value."""
        # Safety check: if list is empty
        if self.tail is None:
            return None

        # Logic 1: Store the value to return later
        value_to_return = self.tail.value

        # Logic 2: If there is only one person in line
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Logic 3: If there are more people
        else:
            self.tail = self.tail.previous  # Move tail back one
            self.tail.next = None           # New tail lets go of the old tail

        # Logic 4: Return the name/value
        return value_to_return