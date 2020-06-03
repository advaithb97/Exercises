from array import array 
array_num = array('i', [5, 8, 12, 15, 10, 7])
greatest = array_num[0]
lowest = array_num[0]
for elem in array_num:
    if elem>greatest:
        greatest = elem
    if elem<lowest:
        lowest = elem
print(greatest-lowest)