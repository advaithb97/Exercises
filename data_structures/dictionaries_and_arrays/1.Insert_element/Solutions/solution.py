from array import array
arr = array('i', [45,21,35,1,93])
ins_pos = int(input("enter position"))
ins_val = int(input("enter value"))
arr.insert(ins_pos, ins_val)
print(arr)