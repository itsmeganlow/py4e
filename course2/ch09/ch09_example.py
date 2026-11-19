name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

top_word = None
top_count = None
for word, count in counts.items():
    if top_count is None or count > top_count:
        top_word = word
        top_count = count

print(top_word, top_count)