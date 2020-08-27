# integer
number_of_phases = 3
print(type(number_of_phases))

# float
pressure_psia = 457.8

# complex
complex_number = 1 + 1.1j

## type conversion to float and str
pressure_in_kpa = input("What is the pressure in kPa? ")
## pressure_in_psia = pressure_in_kpa * 0.14  # generates error
pressure_in_psia = float(pressure_in_kpa) * 0.14
# convert the numeric value back to string to use string concatenation
output = "Reservoir pressure is " + str(pressure_in_psia) + " psia"
print(output)

# quiz How to convert string of float to integer (e.g. user enters 89.0)
n_grids = input("Enter the number of simulation grids? ")
n_grids = int(float(n_grids))  # what if the user enter a float value like 89.0
print("Simulation model has " + str(n_grids) + " grids")