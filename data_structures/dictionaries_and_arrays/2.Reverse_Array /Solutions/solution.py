from array import array
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
reverse_array = array('i')
for i in range(len(array_num)):
    reverse_array.append(array_num[len(array_num) - 1 - i])
print(reverse_array)
