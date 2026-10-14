text = "X-DSPAM-Confidence:    0.8475"
start = text.find(' ')+1
answer = text[start:]
print(float(answer.lstrip()))


# From grader
ipos = text.find(':')
print(ipos)
piece = text[ipos+2:]
print(piece)
value=float(piece)
print(value)