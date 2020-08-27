## without having a dictionary, you should make a note what each value
## presents in a list
# rock_properties = ['sand-stone', 125.3, 0.14, 0.21]  # elements:rock_type, perm, poro, sw

## define a dictionary withn key:value pairs inside {}
rock_prop = {'type': 'sand-stone', 'perm': 125.3, 'poro': 0.14, 'sw': 0.21}
# print(type(rock_prop))

## another method of defining a dictionary is to use dict constructor key=value pair
# rock_prop_2 = dict(_type='sand-stone', perm=125.3, poro=0.14, sw=0.21)
#?? why I didn't use type and used _type instead

## to get the values for a key use curly braces or get method
# permeability = rock_prop['perm']  # if the key doesn't exist, and exception error will be thrown
# porosity = rock_prop.get('poro')  # get method will return None if the key doesn't exist
# print(f"Permeability={permeability}\nPorosity={porosity}")  # \n is of the escape characters in Python

'''
Escape Characters
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
A few common escape characters are below:
\'	Single Quote	
\\	Backslash
\n	New Line	
\t	Tab
'''

## to get the values of a dictionary
prop_values = rock_prop.values()
# print(list(prop_values))  # we can use list function to convert result into list

## to get the values of a dictionary
prop_items = rock_prop.items()
prop_items_list = list(prop_items)
print(f"List of items is 'rock_prop' dictionary: {prop_items_list}")
# print(list(prop_values))  # we can use list function to convert result into list of tuple

## A tuple is an immutable(unchangable) sequence of Python objects.
## Tuples are sequences, just like lists.
## The differences:
##      the tuples cannot be changed unlike lists
##      tuples use parentheses, whereas lists use square brackets.
sws = (0.2, 0.3, .25)
print(f"Type of sws:{type(sws)}")

# perms_tuple = tuple([102.5, 123, 56.01])
# for perm in perms_tuple:
#     print(perm)
