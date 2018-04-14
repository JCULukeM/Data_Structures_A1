from double_linked_list import DoubleLinkedList, ListNode
import ctypes

class SparseArray:

    def __init__(self, _n):
        self._n = _n
        self._A = self.make_array(_n)
        self.store_array = DoubleLinkedList()

    def make_array(self, size):
        return (size * ctypes.py_object)()

    def __setitem__(self, k, value):
        """Insert value at index k"""
        if value is not None:
            self.store_array.add_list_item(ListNode(value , k))
 #       self._A[k] = self._Node(value, k + 1)  # store newest element

    def __getitem__(self, k):
        """Return element at index k."""
        return self.store_array[k]

    def __len__(self):
        return self._n