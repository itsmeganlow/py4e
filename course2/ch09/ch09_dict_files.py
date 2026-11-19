# COUNT WORDS IN A FILE
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split() # REMOVE WHITESPACE AND SPLIT INTO WORDS

print('Words:', words) # GET A LIST OF WORDS FROM THE INPUT LINE

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1 # GET THE VALUE OF THE KEY 'WORD' IF IT EXISTS, OTHERWISE RETURN 0 AND ADD 1 TO IT
print('Counts:', counts)
