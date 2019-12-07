import sys

orbits = {}

# Open the file passed as a command line argument
# Build an object where the keys are the identifiers of the orbiting object
# and the values are the identifiers of the objects they orbit
with open(sys.argv[1]) as f:
    read_orbits = f.readlines()
    for read_orbit in read_orbits:
        center, orbiting_object = read_orbit.strip().split(")")
        orbits[orbiting_object] = center


orbit_count = 0

# For each orbiting object, increment orbit_count by 1. It must orbit something
for key in orbits:
    orbit_count += 1
    # If the thing it orbits orbits something, recurse
    while orbits[key] in orbits:
        orbit_count += 1
        key = orbits[key]

print(orbit_count)
