from positional_array import PositionalList


def main():
    linked_list = PositionalList()
    linked_list.add_first(42)
    linked_list.add_last(55)
    print(linked_list.__iter__())
main()