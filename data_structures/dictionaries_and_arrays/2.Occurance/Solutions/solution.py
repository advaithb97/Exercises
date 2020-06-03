from array import array
array_num = array('i', [15, 30, 45, 60, 75, 90])
element = int(input("Choose element"))
counter = 0
for i in array_num:
    if i == element:
        counter +=1
print(counter)