from sparse_array2 import SparseArray


def main():
    my_list = [1, 9, 17, 18]
    array = SparseArray(100)

    array[50] = 42

    print(array[50])

    array[-1] = 66
    array.fill(my_list)
    print(array[-1])
    print(len(array))
    array[98] = 77

    for element in array:
        print(element)
#    print("{} nodes used".format(array.get_usage()))

main()

