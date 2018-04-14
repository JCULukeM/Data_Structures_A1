from list_node import ListNode


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def __getitem__(self, item):
        current_node = self.head

        while current_node is not None:
            if current_node.is_index(item):
                results = current_node.data
                return results
            current_node = current_node.next

    def add_list_item(self, item):
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        return
