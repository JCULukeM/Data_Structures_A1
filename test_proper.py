from testing import DynamicArray

print((3 >= 3) or (5 < 7) and (9 != 5))
array_one = DynamicArray()
print(array_one)
array_one.append(1)
array_one.append(6)
array_one.append(4)
print(len(array_one))
my_list = []
for element in array_one:
    my_list.append(element)

print(my_list)
