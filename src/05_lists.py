# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)


# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
# print(x)
x.extend(y)
print(x, "x extended")
# print(x.extend(y))

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 

print(x.remove(8))

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(3,99)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print("length", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for val in x:
    print(str(val*1000))

xMultiplied = [x * 100 for x in x]
print(xMultiplied)
