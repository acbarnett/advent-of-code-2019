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

# For each y, for each x, look at all layers
# When a non-transparent layer is found, if it's black, display a " "
# If white, display a 1 and break out of the loop
# Print all of the characters for a row on one line, then add a newline
for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        for layer in layers:
            target_pixel = y * WIDTH + x
            if layer[target_pixel] != "2":
                color = layer[target_pixel]
                if color == "0":
                    color = " "
                print(color, end="")
                break
    print("")
