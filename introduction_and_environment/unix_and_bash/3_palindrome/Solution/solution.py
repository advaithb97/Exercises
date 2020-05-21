line = input()
is_palindrome = True
length = len(line)
for i in range(length):
    if line[i] != line[length-1-i]:
        is_palindrome = False
print(is_palindrome)