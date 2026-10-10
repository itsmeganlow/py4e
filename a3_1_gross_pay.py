hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
rr = float(rate)
o = h - 40 #overtime hours
if h > 40:
    overtimerate = 1.5 * rr
else:
    overtimerate = rr
grosspay = (40 * rr) + (o * overtimerate)
print(grosspay)
