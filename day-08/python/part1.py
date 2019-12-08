import sys

# Set up constants
WIDTH = 25
HEIGHT = 6
LAYER_SIZE = WIDTH * HEIGHT

# Read in the input file and convert to a list
pixel_string = ""
with open("./input.txt") as f:
    pixel_string = f.readline()
unlayered_pixel_values = list(pixel_string.strip())

# Make into a list of layers
idx = 0
layers = []
while idx < len(unlayered_pixel_values):
    layers.append(unlayered_pixel_values[idx:(idx + LAYER_SIZE)])
    idx += LAYER_SIZE

# Find the layer with the fewest zeroes
fewest_zeroes = LAYER_SIZE + 1
layer_with_fewest_zeroes = None
for i, layer in enumerate(layers):
    zeroes = 0
    for pixel in layer:
        if pixel == "0":
            zeroes += 1
    if zeroes < fewest_zeroes:
        fewest_zeroes = zeroes
        layer_with_fewest_zeroes = i

# For the layer with the fewest zeroes, count the ones and twos
# and then print the product of the ones and the twos
layer_of_interest = layers[layer_with_fewest_zeroes]
ones = 0
twos = 0
for pixel in layer_of_interest:
    if pixel == "1":
        ones += 1
    if pixel == "2":
        twos += 1

product = ones * twos
print(product)

