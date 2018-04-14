
class SparseArray:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

        def __str__(self):
            return '{}'.format(self._element)

    """
    constructor(number of elements = 0)
        instance.Element = element
        instance.setArray(element)
    """

    def __init__(self, _n=0):
        self._n = _n
        self._A = self._make_array(self._n)

    """
    method makeArray(size)
        array = [set node(None, index + 1) for index in range(size)]
        array [index -1]setNext = blank
    
    """
    def _make_array(self, size):
        """Return new array with capacity n."""
        array = [self._Node(None, (k + 1)) for k in range(size)]
        array[-1]._next = None
        return array
    """
    method fill(sequence)
        for element in sequence
            array[index] = element
            index += 1
    """

    def fill(self, seq):
        if len(seq) > self._n:
            raise ValueError("Seq longer than array")
        k = 0
        for element in seq:
            self._A[k] = self._Node(element, k +1)
            k += 1
    """
    method getItem(index)
        if index < 0
            index += len(self)
        if not 0 <= k < size of array
            display "invalid index'
        return array[index] node class element
    """

    def __getitem__(self, k):
        """Return element at index k."""
        if k < 0:
            k += len(self)
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]._element  # retrieve from array

    """
    method setItem(index, value)
        array[index] = node(value, index + 1)
    
    """
    def __setitem__(self, k, value):
        """Insert value at index k"""
        self._A[k] = self._Node(value, k + 1)  # store newest element

    """
    Basic getter for length
    """
    def __len__(self):
        return self._n

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
            if i._element is not None:
                non_empty +=1
        return non_empty




