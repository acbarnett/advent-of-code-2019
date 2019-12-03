# Read the list of numbers from a file
# Split on commas, convert to ints
# Returns a list of integers
def read_from_input():
    with open("../input.txt") as f:
        intcode_string = f.readline()
        intcode_string = intcode_string.strip()
        intcode_list = [int(i) for i in intcode_string.split(",")]
        return intcode_list

def return_four():
    return 4

# Given a list of intcode, resolve it into its final form
def process_intcode(intcode):
    return intcode
