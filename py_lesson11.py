# List: A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
# I recommend to use plural names for list variables for later readability
sw_values = [0.23, 0.12, 0.16, 0.18, 0.8, 0.12]  # use brackets to initiate a list
# print(sw_values)

## access items through indexing and slicing
print(sw_values[0])
print(sw_values[:2])
print(sw_values[-1])

## lists are changeable
print(f"original sw_values: {sw_values}")
sw_values[0] = 0.201
print(f"sw_values after changing sw[0]: {sw_values}")

## list can store different data types in one list
reservoir_props = [1234., "ss", 0.34, True]  # average pressure, rock type, avg. sw, is_water_wet
reservoir_props_plus = [1234., "ss", [0.34, 0.66],
                        True]  # average pressure, rock type, [avg. sw, avg. so], is_water_wet
print(f"Reservoir properties: {reservoir_props}")
print(f"Reservoir properties+: {reservoir_props_plus}")

## check the membership
sw_values = [0.23, 0.12, 0.16, 0.18, 0.8]
print(0.2 in sw_values)
print(0.2 not in sw_values)

## some of the list methods
## append(): Used for appending and adding elements to List.It is used to add elements to the last position of List.
sw_values = [0.23, 0.12, 0.16, 0.18, 0.8]
sw_values.append(0.03)
print(f"appended list:{sw_values}")
## insert(): Inserts an elements at specified position.
sw_values.insert(2, 0.)
print(sw_values)

## get the length or the number of items in a list, sum, max and min
print(len(sw_values))
print(sum(sw_values))
print(max(sw_values))
print(min(sw_values))

# ## to remove item from a list
print(f"original sw_values: {sw_values}")
sw_values.pop()  # to remove the last item of the list
print(f"After removing the last item and sw_list: {sw_values}")
sw_values.pop(1)  # to remove the item at specific position of the list
print(sw_values)

## Returns the index of first occurrence.
## Syntax: _list.index(element[,start[,end]])  note:Start and End index are not necessary parameters.
sw_values = [0.23, 0.12, 0.16, 0.18, 0.8]
print(f"Index of 0.16 is: {sw_values.index(0.16)}")

## to create a separate copy use the following command
sw_values = [0.23, 0.12, 0.16, 0.18, 0.8]
sw_values2 = sw_values[:]
sw_values2[0] = 0.1234
print(sw_values)
print(sw_values2)
