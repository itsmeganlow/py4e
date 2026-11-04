# SPLIT
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

# DELIMITERS
line = 'A lot       of spaces'
etc = line.split()
print(etc) # extra spaces are ignored

line = 'first;second;third'
thing = line.split()
print(thing) # no delimiter specified, so it splits on whitespace
print(len(thing)) # length of list is 1

thing = line.split(';')
print(thing) # delimiter is semicolon
print(len(thing)) # length of list is 3