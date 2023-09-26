"""
Problem Set 0 - Einstein
https://cs50.harvard.edu/python/2022/psets/0/einstein/
"""

# Prompt the user for mass as an integer (in kilograms)
mass = int(input("Enter mass in kilograms: "))

# Calculate energy using E = mc^2
c = 300000000
energy = mass * c ** 2

# Print the energy
print(energy)

