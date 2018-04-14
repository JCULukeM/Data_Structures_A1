class ListNode:
    def __init__(self, data, index):
        self.data = data
        self.next = None
        self.previous = None
        self.index = index
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

    def is_index(self, index):
        if self.index == index:
            return True
        else:
            return False

    def return_index(self):
        return self.index