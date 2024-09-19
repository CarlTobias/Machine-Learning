# List Operations

print("List Operations\n\n")


numList = [16, 28, 5, 8, 29]
largest = numList[0]

for n in numList:
    if n > largest:
        largest = n

print(numList)
print(n, "is the largest number in the list.\n")