# Arithmetic operators
x = 10.0
y = 3.1415
exponent = 3
print("sum:", x + y)  # addition
print("subtraction:", x - y)  # addition
print("multiplication:", x * y)  # multiplication
print("float division:", x / y)  # float division
print("floor division:", int(x) // int(y))  # floor division
print("modulus:", int(x) % int(y))  # modulus: the remainder when first operand is divided by the second
print("exponent:", x ** exponent)  # exponent

# the result of a mathematical expression can be assigned to a new variable
z = x + y
# Use mathematical operation to modify the value of a variable in place
print("before modify: x=", x)
x = x / 2
print("after modify: x=", x)

# each arithmetic operator has an augmented operator equivalent
#y = y + 2
y += 2  # this is equivalent to y = y + 2
y **= 2
print("y=", y)

sw = 0.2
so = 0.45

# un-equality
print(sw != 0.2)

# less than
print(sw < so)

# returns True if both statements are true
print(sw > 0.1 and so < 0.3)

# returns True if one of the statements is true
print(sw > 0.15 or so > 0.60)

# negate the result, returns False if the result is true
print(not sw <= 0.1)
