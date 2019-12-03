# Read the list of numbers from a file
# Split on commas, convert to ints
# Returns a list of integers
def read_from_input():
    with open("../input.txt") as f:
        intcode_string = f.readline()
        intcode_string = intcode_string.strip()
        intcode_list = [int(i) for i in intcode_string.split(",")]
        return intcode_list

def process_1202_program(intcode_input):
    intcode = intcode_input[:]
    intcode[1] = 12
    intcode[2] = 2
    return intcode

END_OP = 99
ADD_OP = 1
MULT_OP = 2

# Given a list of intcode, resolve it into its final form
def process_intcode(intcode_input):
    # Clone the list, to prevent any spooky mutability shenanigans
    intcode = intcode_input[:]

    pos = 0
    op = intcode[pos]

    while op is not END_OP:
        input_pos_1 = intcode[pos + 1]
        input_pos_2 = intcode[pos + 2]
        dest = intcode[pos + 3]
        if op is ADD_OP:
            intcode[dest] = intcode[input_pos_1] + intcode[input_pos_2]
        if op is MULT_OP:
            intcode[dest] = intcode[input_pos_1] * intcode[input_pos_2]
        pos = pos + 4
        op = intcode[pos]

    return intcode

