from without_node import SparseArray
from random import randint
import sys


def seq_to_node(my_list, single_list):
    a = 0
    for element in my_list:
        a += 1
        if element is not None:
            single_list.append(a + element)


def get_sequence(sparse_array_list):
    for i in range(1,102):
        number = randint(1,100)
        if number % 2 == 0:
            sparse_array_list.append(None)
        else:
            sparse_array_list.append(number)


def main():
    sparse_array_list = []
    array = SparseArray(1000)

    print("The array contains {} elements".format(array.__len__()))
    b = sys.getsizeof(array)
    print("Size in bytes is {}".format(b))

    get_sequence(sparse_array_list)
    array.fill(sparse_array_list)
    index = 0
    for element in array:
        print("{}idx - {}".format(index,element))
        index += 1
    print("index 90 is {}".format(array.__getitem__(-1)))

    b = sys.getsizeof(array)
    print("Size in bytes is {}".format(b))
#    print("This array contains {} non-empty elements".format(array.get_usage()))
    print("The array contains {} elements".format(array.__len__()))


main()
