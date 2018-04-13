from sparse_array import SparseArray


def main():
    array = SparseArray(100)
    array[50] = 42
    print(array[50])
    print(len(array))
    array[98] = 66
    for element in array:
        print(element)
    print("{} nodes used".format(array.get_usage()))

main()

