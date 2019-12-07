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

# Find a path from the object you intend to reach to the center of your system
# The object it is immediately orbiting is at index 0
san_to_center = []
san_location = "SAN"
while san_location in orbits:
    san_to_center.append(orbits[san_location])
    san_location = orbits[san_location]

# Find the path from you to the center of the system
# The object you are orbiting is at index 0
you_to_center = []
you_location = "YOU"
while you_location in orbits:
    you_to_center.append(orbits[you_location])
    you_location = orbits[you_location]

# Assume the paths don't intersect
# For every point on your path to the center, see if it
# is also in the path from your destination to the center
# Add the distances
distance = None
for idx, loc in enumerate(you_to_center):
    if loc in san_to_center:
        distance = idx + san_to_center.index(loc)
        break

print(distance)
