# # well address: lsd-section-township-range-westing
#
# # original string variable
# well_address = '13-28-035-02W5'
#
# # to verify that well_address is of type string use type function
# print("variable type:", type(well_address))
#
# # extract well range (just provide one index)
# well_westing = well_address[-1]
# print("well westing:", well_westing)
#
# # extract well LSD
# well_lsd = well_address[0:2]
# print("well lsd:", well_lsd)
#
# # extract well Westing
# well_range = well_address[-4:-2]
# print("well range:", well_range)
#
# # the default start index is 0 (if omitted, 0 will be considered)
# well_lsd_2nd_approach = well_address[:2]
# print("well lsd - second approach:", well_lsd_2nd_approach)
#
# # the default stop index is n-1 (if omitted, the last index will be considered)
# well_address_without_lsd = well_address[3:]
# print("well without lsd:", well_address_without_lsd)
#
# # provide step for slicing
# well_dummy_att = well_address[0:8:3]
# print("well dummy attribute:", well_dummy_att)
#
# # to reverse the string, provide step -1
# well_address_reversed = well_address[::-1]
# print("well address reversed:", well_address_reversed)
#
# # to get a new copy of the original string variable
# well_address_copy = well_address[::]
# print("well address copy version:", well_address_copy)


## use + to combine two strings and return a new string
# well_lsd = "06"
well_section = "03"
# well_address = well_lsd + "-" + well_section
# print("well address: ", well_address)

## if a string is multiplied by an integer n, string is repeated n times.
# repeated_well_section = well_section * 5
# print("After repeating the string 5 times:", repeated_well_section)

## original string
well_info = "Abandoned Gas well - Field_A"

## len() function will give you the length of string(sequence)
# well_info_length = len(well_info)
# print("length of", well_info, ":", well_info_length)

## to convert a string to lower case
# well_info_lower_case = well_info.lower()  # a function after dot is called method
# print(well_info, "with lower() method>>", well_info_lower_case)

## to convert a string to upper case
# well_info_upper_case = well_info.upper()
# print(well_info, "with upper() method>>", well_info_upper_case)

## to convert a string to upper case
# well_info_titled = well_info.title()
# print(well_info, "with title() method>>", well_info_titled)

## to find the index of a character in string
# index_character = well_info.find("G")  # find the first index where "g" located
# print("Character G was located at index: ", index_character)

## to replace part of a string with another string
# well_info_replaced = well_info.replace("Gas", "Oil")
# print(well_info, "with replace() method>>", well_info_replaced)

## to split a string into multiple strings
# well_info_details = well_info.split("-")
# print(well_info, "with split() method>>", well_info_details)

## to check if a phrase or character exists in a string
print('well' in well_info)  # result will be boolean value
print('wellbore' in well_info)  # result will be boolean value
print('W' not in well_info)  # results will be boolean value
print('w' not in well_info)  # results will be boolean value
