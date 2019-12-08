from itertools import repeat

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

#image = list(repeat(list(repeat("2", WIDTH)), HEIGHT))

image = []
for i in range(0, HEIGHT):
    image.append(list(repeat("2", WIDTH)))

print(image)



for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        color = "2"
        for layer in layers:
            target_pixel = y * WIDTH + x
            #print(layer[target_pixel])
            if layer[target_pixel] != "2":
                color = layer[target_pixel]
                if color == "0":
                    color = " "
                print(color, end="")
                break
    print("")
                
        
#for x in range(0, width):
#for y in range(0, height)

#print(image[24][2])
#print(image[2][24])

#layer_ct = len(layers)
#for y in range(0, HEIGHT):
#    for x in range(0, WIDTH):
#        color = 0
#        for layer in layers:
            #print(layer)
 #           target_pixel = layer[y * WIDTH + x]
#            if target_pixel != "2":
   #             color = target_pixel
  #              break
#        print(target_pixel, end = '')
        #print([y,x,color])
#    print("")
    #    image[y][x] = color


#for row in image:
#    row_as_strs = [str(px) for px in row]
#    print("".join(row_as_strs))

#
