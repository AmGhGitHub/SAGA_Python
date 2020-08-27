## open a file
## if for the mode keyword you use 'r' the file should exist
# if the file doesn't exist, an exception will be thrown
# with open('property_values.txt', 'r') as file:
#     all_lines = file.read()
#     print(all_lines)

# an easier way to read file content line by line
# with open('property_values.txt', 'r') as file:
#     for line in file:
#         print(line, end='')  # what is the functionality of end=''

## use readlines to return the file content as list
# with open('property_values.txt', 'r') as f:
#     lines_as_list = f.readlines()
#     print(lines_as_list)

# ## the above syntax can be simplified as:
# with open('property_values.txt', 'r') as file:
#     lines_as_list = list(file)
#     print(lines_as_list)

sws = [0.2, 0.21, 0.09, 0.05]
## if you use mode 'w' to write to a file, file will be first created if doesn't exist
with open('water_saturation.txt', mode='w') as writer:
    writer.writelines(str(sws))  # or writer.writelines(f"{sws}")

with open('water_saturation_2.txt', 'w') as writer:
    for sw in sws:
        writer.write(f"{sw}, ")
