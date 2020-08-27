pressure_psia = [1250.145, 629, 7850.2, '450.6', 14.7, '1287.02', 844.1]
length_pressure = len(pressure_psia)

## while loop with float conversion
# index = 0
# while index < length_pressure:
#     pressure_kpa = float(pressure_psia[index]) * 6.89476
#     print(f"{float(pressure_psia[index]):0.2f} psia = {pressure_kpa:,.3f} kPa")
#     index += 1  # if you forget this line (to increase index value), loop will be infinite
# else:
#     print("All pressure conversions were completed!\n")


## break the loop if non-numeric input was encountered
# index = 0
# while index < length_pressure:
#     # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#     if isinstance(pressure_psia[index], str):
#         break
#     pressure_kpa = pressure_psia[index] * 6.89476
#
#     print(f"{float(pressure_psia[index]):0.2f} psia = {pressure_kpa:,.3f} kPa")
#     index += 1  # if you forget this line (to increase index value), loop will be infinite
# else:
#     print("All pressure conversion was completed!")
# print("Please notice, in case of break, 'else' statement was ignored!\n")

## jump over non-numeric values using continue and do conversion for the numeric inputs
# index = 0
# while index < length_pressure:
#     # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#     if isinstance(pressure_psia[index], str):
#         index += 1  # Don't forget to change your iterator value
#         continue
#     pressure_kpa = pressure_psia[index] * 6.89476
#     print(f"{float(pressure_psia[index]):0.2f} psia = {pressure_kpa:,.3f} kPa")
#     index += 1
# else:
#     print("All pressure conversions for numeric values were completed!")


## use range() function in for-loop
## to generate square values in range of 0 to 6(exclusive)
# square_values = []
# for i in range(6):
#     square_values.append(i ** 2)
# print(square_values)
#
# sw_values = [0.2, 0.25, 0.56]
# so_values = []
#
# for sw_value in sw_values:
#     so_values.append(1.0 - sw_value)
# else:
#     print(so_values)
#
work_desc = 'PeTrOLeUm EnGiNeErS AnD GeOlOgIsTs'
work_desc_mod = ""
for character in work_desc:
    if character.isupper():
        work_desc_mod += character.lower()
    else:
        work_desc_mod += character.upper()
print(work_desc_mod)
