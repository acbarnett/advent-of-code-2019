from intcode_lib import process_1202_program, process_intcode, read_from_input

intcode_from_file = read_from_input()
intcode_input = process_1202_program(intcode_from_file)
processed_intcode = process_intcode(intcode_input)

print(processed_intcode[0])

