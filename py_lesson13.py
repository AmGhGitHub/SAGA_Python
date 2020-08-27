has_high_permeability = False

# if has_high_permeability:
#     print("Good reservoir quality and profitable asset")  # notice the indention
# else:
#     print("Poor reservoir quality and not a profitable asset")  # notice the indention
#
# print("Senior Geologist's Assessment")


wti_price = 56.0
is_heavy_oil = False

# Do we really need the else statement here?
price_differential = 8.5
if is_heavy_oil:
    price_differential = 14.5


oil_price = wti_price - price_differential

# print(f"Today's oil price: ${oil_price} based on ${price_differential} differential.")

blocks_sat = [0.5, 0.15,0.4]  # let's say it presents: [so, sw, sg] where so+sw+sg=1.0

# if expression:
# ----block code
sum_sat = sum(blocks_sat)
length_sat = len(blocks_sat)

# if length_sat > 3:
#     print("Max 3 values are required.")
# elif length_sat < 3:
#     print("Min 3 values are required.")
# else:
#     if sum_sat <= 1.0:
#         print(f"Summation is: {sum_sat:.2f}")
#     else:
#         print("Summation>1.0! Please normalize!")

# logical conditions
# Logical operators
# logical and; logical or; logical not
# AND: both
# OR: at least one
# Not: Inverse the boolean value
wti_price = 56.0
is_heavy_oil = True
is_sour = True

# nested if statement
if is_heavy_oil or is_sour:  # at least one
    price_differential = 12.5  # base differential price
    if is_heavy_oil and is_sour:
        price_differential += 2.0
    elif not is_heavy_oil and is_sour:
        price_differential -= 2.0
else:  # neither heavy nor sour
    price_differential = 8.5

oil_price = wti_price - price_differential

print(f"Today's oil price is ${oil_price} based on ${price_differential} differential.")
