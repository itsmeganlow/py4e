fruit = 'banana'
x = len(fruit) # len() gives you the number of characters in a string:
print(x)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

fruit = 'banana'
for letter in fruit: # iterate through each character in a string aka iteration variable
    print(letter)
#a definite loop using for statement is much more elegant and more direct and succinct

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)