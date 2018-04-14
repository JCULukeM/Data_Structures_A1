from time import time
from sparse_array import SparseArray
from random import randint


def get_sequence(array):
    """Fills array with random numbers and empty nodes"""
    for i in range(1, 50):
        number = randint(1, 100)
        array[randint(1, len(array) -1)] = number


def main():
    experiment_result = []
    value = 3
    array = SparseArray(10 ** 7)


    while value > 0:
        value -= 1
        index_value = randint(1, len(array) - 1)
        start_time = time()
        get_sequence(array)
        end_time = time()
        elapsed = end_time - start_time
        experiment_result.append(elapsed)
    print(experiment_result)
    print(array.get_usage())

main()