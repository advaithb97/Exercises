x = 40
arr = []
for i in range(1,x+1):
    if i//7 == 0 and i//5 == 0:
        arr.append(i)
print(arr)