# SPLIT AND PARSE
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

# DOUBLE SPLIT
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split() 
    email = words[1] # stephen.marquad@uct.ac.za
    pieces = email.split('@') # ['stephen.marquad', 'uct.ac.za']
    print(pieces[1]) # 'uct.ac.za'