string = "BYTE ACADEMY"
vowels = ['aeiou']
data = ""
for letter in string:
    if letter not in vowels:
        data += letter