class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass