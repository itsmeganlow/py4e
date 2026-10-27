fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

#generates a lot of blank lines because print func adds a new line
#and end of the text line already comes with a blank line too
#thus, use rstrip

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#r.strip strips whitespace from right hand side of the string

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#continue generates the same result
#it just skips through the lines we arent interested in and print only good lines that we want

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)