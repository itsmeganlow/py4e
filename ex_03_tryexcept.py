score = input("Enter score: ")
try:
    score = float(score)
except:
    print("Invalid input")
    exit()  #program exits if the input is not a valid float number.
print("You scored", score)