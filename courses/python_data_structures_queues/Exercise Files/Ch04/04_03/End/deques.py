class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Takes an item as a parameter and inserts it into the 0th index
        of the list that is representing the Deque.

        The runtime is linear, or O(n), because every time you insert into the
        front of a list, all the other items in the list need to shift one
        position to the right.
        """

        self.items.insert(0, item)

    def add_rear(self, item):
        """Takes in an item as aparameter and appends that item to the end of
        the list that is representing the Deque.

        The runtime is constant because appending to the end of a list happens
        in constant time.
        """

        self.items.append(item)

    def remove_front(self):
        pass

    def remove_rear(self):
        pass

    def peek_front(self):
        pass

    def peek_rear(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass
