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
        """Removes and returns the last item for the list, which is also the
        top item of the Stack.

        The runtime here is constant time, because all it does is index to the
        last item of the list.
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass