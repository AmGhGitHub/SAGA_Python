## using list comprehension
G_CONSTANT = 9.81  # acceleration gravity value
rho_oil = 897.0  # oil density, [kg/m3]
rho_water = 999.0  # oil density, [kg/m3]
woc_m = 1200
depths = [1000, 1110, 1130.5, 1156, 1200]

##using for loop to create list of static pressures
static_pressure = []
for depth in depths:
    static_pressure.append(depth * rho_oil * G_CONSTANT * 0.001)
# print(f"Append Method:{static_pressure}")
##Using list comprehension
static_pressure_2 = [depth * rho_oil * G_CONSTANT * 0.001 for depth in depths]
# print(f"Comprehension Method: {static_pressure_2}")

depths = [1000, 1110, 1130.5, 1156, 1200, 1400, 1430.7]
## conditional list comprehension
static_pressure_cond = [depth * rho_oil * G_CONSTANT if depth <= woc_m
                        else depth * rho_water * G_CONSTANT for depth in depths]
print(static_pressure_cond)