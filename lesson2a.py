# Python lists
# A list in python is a collection of items that are odered in a certain way
# A list is introduced by the use of the square brackets {}.
# The items of a list are stored inside of indexes. Note: In programming we start counting from index Zero(0).
# A list is mutable i.i the contents of a list can be changed.

cars=["BMW", "Benze", "Hiance", "Prado", "Probox", "Mclaren", "Range"]

print(cars)
print(type(cars))

# Accessing items of a list
print(cars[2])
print("The car on index four is: ", cars[4])



# List slicing- This is creating a list from a given bigger list
print(cars[4:])

# Printing from index zero to three
print(cars[:4])

# Printing from hiance to probox
print(cars[2:5])

# List- Mutability
# We use the function append to add an item at the end of a list
cars.append("mercedes")
print(cars)
cars.append("subaru")
print(cars)

# We use the pop function to remove an item from the end of the list.
cars.pop()
print(cars)

# We can use an index to add items to a list
cars[5]=("Pajero")
print(cars)

# We can use the sort function to sort out the items in alphabetical order
cars.sort(reverse=True)
print(cars)

cars.remove("BMW")
print(cars)