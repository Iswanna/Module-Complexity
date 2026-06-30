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
