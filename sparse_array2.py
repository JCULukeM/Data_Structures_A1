from double_linked_list import DoubleLinkedList, ListNode
import ctypes


class SparseArray:

    """
    constructor(number of elements = 0)
        instance.Element = element
        instance.setArray(element)
    """
    def __init__(self, _n):
        self._n = _n
        self._A = self.make_array(_n)
        self.store_array = DoubleLinkedList()

    """
    Method make_array(size)
        return low level array the length of size
    """

    def make_array(self, size):
        return (size * ctypes.py_object)()

    """
    Method setItem(index, value)
        if index < 0
            index += length of self
        if value is not blank
            add ListNode object(value, index) in store_array with add_list_item method
    """

    def __setitem__(self, k, value):
        """Insert value at index k"""
        if k < 0:
            k += len(self)
        if value is not None:
            self.store_array.add_list_item(ListNode(value , k))

    """
    method getItem(index)
        if index < 0
            index += length of self
        if not 0 <= index < size of array
            display IndexError 'invalid index'
        return store_array[index]
    """

    def __getitem__(self, k):
        """Return element at index k."""
        if k < 0:
            k += len(self)
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self.store_array[k]

    """
    Basic getter for length
    """

    def __len__(self):
        return self._n

    """
    method fill(sequence)
        if length of sequence > size of array
            display value error 'Seq longer than array'
        index = 0
        for element in sequence
            store_array[index] add_list_item method(ListNode class(element,
    """
    def fill(self, seq):
        if len(seq) > self._n:
            raise ValueError("Seq longer than array")
        k = 0
        for element in seq:
            self.store_array.add_list_item(ListNode(element, k))
            k += 1

    """
    method getUsage()
        nonEmpty = 0
        for object in array
            if object.node_element is not blank
                non_empty += 1
        return non_empty
        """

    def get_usage(self):
        non_empty = 0
        for i in self._A:
            if i is not None:
                non_empty +=1
        return non_empty
