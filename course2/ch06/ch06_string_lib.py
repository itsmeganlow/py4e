greet = 'Hello Bob'
zap = greet.lower() # convert to lower case
print(zap)
print(greet) # original string is not changed

print('Hi There'.lower()) # can also be used on string literals

print('Hello Bob'.upper()) # convert to upper case

fruit = 'banana' 
pos = fruit.find('na') # find() returns the index of the first occurrence of the substring, or -1 if not found
print(pos)

aa = fruit.find('z')
print(aa)

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane') # replace() returns a new string with
print(nstr)

nstr = greet.replace('o', 'x') # replace() can also be used to replace all occurrences of a character
print(nstr)

greet = '    Hello Bob.   '
print((greet.lstrip()))
print((greet.rstrip()))
print((greet.strip()))

line = 'Please have a nice day'
line.startswith('Please') # gives True
line.startswith('p') # gives False

data = 'From stephen.marquard@uct.ac.za Sat Jan 2 2007'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)