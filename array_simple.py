from sparse_array2 import SparseArray


def main():
    my_list = [1, 9, 17, 18]
    array = SparseArray(100)

    array[50] = 42

    print(array[50])

    array[40] = 66

    print(array[40])
    """print(len(array))
    array[98] = 66
    for element in array:
        print(element)
    print("{} nodes used".format(array.get_usage()))"""

main()

