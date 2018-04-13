import ctypes

class SparseArray:

    def __init__(self, _n):
        self._n = _n
        self._A = self._make_array(self._n)

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def fill(self,seq):
        for element in seq:
            self._A[self._n] = element
            self._n += 1

    def __getitem__(self, k):
        """Return element at index k."""
        if k < 0:
            k += len(self)
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]  # retrieve from array

    def __setitem__(self, k, value):
        """Insert value at index k"""
        self._A[k] = value  # store newest element
#        self._n += 1

    def __len__(self):
        return self._n

    def get_usage(self):
        non_empty = 0
        for item in self._A:
            if self._A[item] is None:
                non_empty += 1
        return non_empty
