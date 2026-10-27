fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#ask python to open file names but what happens if you open bad file names

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

#this helps to prevent traceback errors becuase it quits

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)