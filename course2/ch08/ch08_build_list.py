# APPENDING TO A LIST
stuff = list() # this creates an empty list []
stuff.append('book')
stuff.append(99)
print(stuff)

# IS SOMETHING IN A LIST?
some = [1, 9, 21, 10, 16]
9 in some # >> True
20 in some # >> False1
# returns True if the value is in the list, False otherwise

# LISTS ARE IN ORDER
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort() # arranges the list in alphabetical order
print(friends)
print(friends[1])

# LEN/MAX/MIN/SUM
nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) 
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums)) # average

## EXAMPLE 1
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

## EXAMPLE 2
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)

# tiny difference between the two examples is that in the first example 
# we keep a running total and count, while in the second example we store all the numbers in a list 
# and use sum() and len() to compute the average.