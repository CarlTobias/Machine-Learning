# Exeption Handling

print("Exeption Handling\n\n")


try:
    numInput = input("Enter a number: ")
    convertNum = int(numInput)
    
    print("\nYay, your number has been converted!\n")

except ValueError:
    print("\nOh no! The input is not convertible to int. Try again.\n")