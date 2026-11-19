# GET THE KEYS, VALUES, AND ITEMS OF A DICTIONARY
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))

print(list(jjj.keys()))
print(list(jjj.values()))
print(list(jjj.items())) # TUPLES OF KEY : VALUE PAIRS

# TWO ITERATION VARIABLES
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa, bbb in jjj.items():
    print(aaa, bbb) # PRINTS THE KEY AND VALUE OF EACH ITEM IN THE DICTIONARY
    