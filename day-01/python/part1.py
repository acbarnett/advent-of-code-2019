# Calculate fuel per module as per README
def calculate_fuel(mass):
    return (mass // 3) - 2

# Read in the input file
with open("./input.txt") as f:
    module_masses = f.readlines()

# Remove any possible newlines / trailing spaces
module_masses = [m.strip() for m in module_masses]
# Convert masses into 'int' types for division
module_masses = [int(m) for m in module_masses]

total_fuel_required = 0
for m in module_masses:
    total_fuel_required += calculate_fuel(m)

print(total_fuel_required)

