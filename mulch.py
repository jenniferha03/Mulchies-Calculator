"""
mulch.py
"""

import math

MINIMUM_CUBIC_YARDS = 3
DELIVERY_CHARGE_PER_MILE = 4.25
MINIMUM_DELIVERY_CHARGE = 35
SALES_TAX_RATE = 0.07

print("")
print("Mulch Cost Calculator")
print("=====================")
print("")

length_in_feet = float(input("Enter the length of the planting bed, in feet: "))
width_in_feet = float(input("Enter the width of the planting bed, in feet: "))
depth_in_inches = float(input("Enter the desired depth of mulch, in inches: "))

cubic_yards = math.ceil(float((length_in_feet * width_in_feet * (depth_in_inches / 12))) / 27)

print("")
print("Total much required is approximately", cubic_yards, "cubic yards.")

if cubic_yards < MINIMUM_CUBIC_YARDS:
    CUBIC_YARDS = MINIMUM_CUBIC_YARDS
    print("The minimum mulch order is", MINIMUM_CUBIC_YARDS, "cubic yards.")

print("")
distance = int(input("Enter your distance from Naperville, IL, in miles: "))

print("")
if cubic_yards < MINIMUM_CUBIC_YARDS:
    CUBIC_YARDS = MINIMUM_CUBIC_YARDS
    print("Cost for", MINIMUM_CUBIC_YARDS, "cubic yards of mulch")
else:
    print("Cost for", cubic_yards, "cubic yards of mulch")

delivery_charge = float(distance * DELIVERY_CHARGE_PER_MILE)

MULCH_COST = 0.0

# if delivery_charge < MINIMUM_DELIVERY_CHARGE:
#     delivery_charge = MINIMUM_DELIVERY_CHARGE

DELIVERY_CHARGE = max(delivery_charge, MINIMUM_DELIVERY_CHARGE)

if cubic_yards <= 5:
    mulch_cost = cubic_yards * 36
elif cubic_yards <= 10:
    mulch_cost = (5 * 36) + (cubic_yards - 5) * 33
else:
    mulch_cost = (5 * 36) + (5 * 33) + (cubic_yards - 10) * 30

sales_tax = float(mulch_cost * SALES_TAX_RATE)

total_cost = float(mulch_cost + sales_tax + delivery_charge)

print("================================")
print("          Mulch: $", format(mulch_cost, "8,.2f"))
print("Delivery charge: $", format(delivery_charge, "8,.2f"))
print("      Sales tax: $", format(sales_tax, "8,.2f"))
print("     Total cost: $", format(total_cost, "8,.2f"))
