# f-strings are string literals that have an f at
# the beginning and curly braces containing expressions
# that will be replaced with their values.

so = 0.2
sw = 1 - so
msg = "if so=" + str(so) + " then sw=" + str(sw)
#print(f"if so={so} then sw={1.0 - so}")

output = f"{10 * 90 / 56.8:.3f}"
#print(output)

field_name = "Lake-A"
reservoir_name = "Cardium"
avg_porosity_frc = 0.1263
avg_permeability_md = 1309.78

# without f-string
pool_desc = reservoir_name + " reservoir located in the " + field_name + " field has" + \
            " a porosity of " + str(avg_porosity_frc) + \
            " and a permeability of " + str(avg_permeability_md) + " md."
pool_desc_f = f"{reservoir_name} reservoir located in the {field_name} field " \
              f"has a porosity of {avg_porosity_frc} and a permeability of {avg_permeability_md} md."
print(pool_desc)
print(pool_desc_f)

field_name = "Lake-A"
reservoir_name = "Cardium"
avg_porosity_frc = 0.1263
avg_permeability_md = 1309.78

# how to modify values and format them with f-string
pool_desc_formatted = f"{reservoir_name} reservoir " \
                      f"located in the {field_name} field " \
                      f"has a porosity of {avg_porosity_frc / 0.85:.2f} " \
                      f"and a permeability of {avg_permeability_md ** 1.023:.3e} md."
print(pool_desc_formatted)

# 3.1415926	{:.2f}	2 decimal places ==> 3.14
# 3.1415926	{:+.2f}	2 decimal places with sign ==> 3+3.14
# -1	{:+.2f}	2 decimal places with sign ==> -1.00
# 2.71828	{:.0f}	No decimal places ==> 3
