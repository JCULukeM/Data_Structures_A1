from time import time
from sparse_array2 import SparseArray
from random import randint


def make_sequence(array):
    """Fills array with random numbers and empty nodes"""
    for i in range(1, 50000):
        number = randint(1, 100)
        array[randint(1, len(array) -1)] = number


def main():
    experiment_result = []
    value = 3

#    array_size = int(input("How long should the array be?: "))
#    array = SparseArray(array_size)

    array = SparseArray(10 ** 3)
    make_sequence(array)
    while value > 0:
        value -= 1
        index_value = randint(1, len(array) - 1)

        start_time = time()
        """Place method to test here"""
        print(array[index_value])
        end_time = time()

        elapsed = end_time - start_time
        experiment_result.append(elapsed)
    print(experiment_result)
#    print(array.get_usage())

main()