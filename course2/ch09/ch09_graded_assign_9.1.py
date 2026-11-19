name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split() # chop up the lines into words
    email = words[1] # grab the email address from the second word
    senders[email] = senders.get(email, 0) + 1 #   ③ save it        ① look up current count   ② add 1 like a tally sheet

top_sender = None
top_count = None
for email, count in senders.items():
    if top_count is None or count > top_count:
        top_sender = email
        top_count = count

print(top_sender, top_count)