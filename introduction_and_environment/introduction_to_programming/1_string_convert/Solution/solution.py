string = input("Enter a string: ")
data = string
if string.isupper():
    data = string.lower()
else:
    data = string.upper()

print(data)