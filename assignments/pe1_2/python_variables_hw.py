""""


Assignment
----------
variables and converting


 Create a Python program that converts kilograms to pounds. 
 Use at least four different samples to convert. A sample of the math is provided below,
   do not use the same example in your program. 

   
Kilograms to Pounds Conversion:
-------------------------------
To convert kilograms (kg) to pounds (lb), you can use the following formula:

Pounds (lb) = Kilograms (kg) * 2.20462

Let's calculate the conversion for 5 kilograms


Pseudocode:
-----------
Kilograms (kg): 5 kg
Conversion Factor: 2.20462

Pounds (lb) = 5 kg * 2.20462 ≈ 11.0231 lb

So, 5 kilograms is approximately equal to 11.0231 pounds.

"""

# Define variables for kilogram values
kg_value_1 = 6
kg_value_2 = 7
kg_value_3 = 8
kg_value_4 = 9

# Conversion factor: 1 kilogram = 2.20462 pounds conversion_factor = 2.20462

# Calculate pounds for each kilogram value
conversion_factor = 2.20462
pounds_1 = kg_value_1 * conversion_factor
pounds_2 = kg_value_2 * conversion_factor
pounds_3 = kg_value_3 * conversion_factor
pounds_4 = kg_value_4 * conversion_factor

# Output the results
print(f"{kg_value_1} kilograms is equal to {pounds_1:.2f} pounds")
print(f"{kg_value_2} kilograms is equal to {pounds_2:.2f} pounds")
print(f"{kg_value_3} kilograms is equal to {pounds_3:.2f} pounds")
print(f"{kg_value_4} kilograms is equal to {pounds_4:.2f} pounds")