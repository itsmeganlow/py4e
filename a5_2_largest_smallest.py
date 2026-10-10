largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break #break statement is used to exit the loop when the user inputs "done".
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue #continue breaks out of the current iteration of the loop and goes to the next iteration. It is used here to skip the rest of the code in the loop when an invalid input is encountered.
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)