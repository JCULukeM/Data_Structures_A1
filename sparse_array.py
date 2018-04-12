import ctypes


class SparseArray:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, _n):
        self._n = 0
        self._Node(74, 0)
        self._capacity = 1000
        self._A = self._make_array(self._capacity)

    def make_node_list(self):
        node_list = []
        for i in range (1, self._n):
            node_list.append(self._Node(None, 0))
    def fill(self,seq):
        for element in seq:
            self._A[self._n] = element
            self._n += 1

    def __getitem__(self, k):
        """Return element at index k."""
#        if k < 0:
#            k += len(self)
#        if not 0 <= k < self._n:
#            raise IndexError('invalid index')
#        return self._A[k]  # retrieve from array
        return self._A[self._Node(k, None)]

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __setitem__(self, k, value):
        """Insert value at index k"""
        self._A[k] = self._Node(value, self._A[k + 1])  # store newest element
        self._n += 1

    def __len__(self):
        return self._n

    def get_usage(self):
        non_empty = 0
        for element in self._A[self._n]:
            if element is not None:
                non_empty += 1
        return non_empty
