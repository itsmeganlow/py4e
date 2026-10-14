for letter in 'banana':
    print(letter)

fruit = 'banana'
'n' in fruit # check if a character is in a string
print('Found it!')

s = 'Monty Python'
print(s[0:4]) # use ':' to get a slice of a string
print(s[6:7]) # ':' up to but not including!
print(s[6:20]) # if the index is out of range, it stops at the end of the string

s = 'Monty Python'
print(s[:2]) # if the first index is omitted, it starts at the beginning of the string
print(s[8:12]) # if the second index is omitted, it goes to the end of the string
print(s[:]) # if both indices are omitted, it returns the entire string
