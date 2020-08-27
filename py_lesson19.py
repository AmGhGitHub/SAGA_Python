## syntax error
# first_value = 1
# second_value = 2
# print(f"Summation= {first_value + second_value}")
# ## what if you forget the "+" sign
# print(f"Summation= {first_value  second_value}")
#
# ## Exception error
# first_value = 1
# second_value = 0.0

# try:
#     first_value /= second_value
# except Exception as e:
#     print(e)
# print("An error just happened!")

# print("statement after division")

try:
    value = 1 / 0
    file = open('some_file.txt')
except ZeroDivisionError as e: # place more specific exception at the beginning
    print(e)
    print("my custom message for ZeroDivision exception")
except FileNotFoundError as e:
    print(e)  # internal msg asscoiated with FileNotFoundError exception
    # print("Hey, I couldn't find your file")  # custom message
except Exception as e:  # more general exception at the end
    print(e)
else:
    print("I am in the 'else' block")
finally:
    print("I am in the 'finally' block")
