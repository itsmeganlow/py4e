# COUNTING WITH DICTIONARIES
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1 # INCREMENTING THE VALUE OF THE KEY 'CWEN' BY 1
print(ccc)

# COUNTING WITH A FOR LOOP
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1 # INITIALIZE THE VALUE OF THE KEY 'NAME' TO 1
    else:
        counts[name] = counts[name] + 1 # IF IT IS ALREADY IN THE DICTIONARY, INCREMENT THE VALUE OF THE KEY 'NAME' BY 1
print(counts)

# COUNTING WITH THE GET METHOD
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1 # GET THE VALUE OF THE KEY 'NAME' IF IT EXISTS, OTHERWISE RETURN 0 AND ADD 1 TO IT
print(counts)

# GET is a method that returns the value for a given key if it exists in the dictionary. If the key does not exist, it returns a default value (in this case, 0). 
# This allows us to simplify the counting logic by avoiding the need for an explicit check to see if the key is already in the dictionary.

