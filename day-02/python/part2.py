from intcode_lib import extract_answer, process_intcode, read_from_input

intcode_from_file = read_from_input()

DESIRED_OUTPUT = 19690720

def modify_input(intcode_input, noun, verb):
    intcode = intcode_input[:]
    intcode[1] = noun
    intcode[2] = verb
    return intcode

def naive_search():
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = process_intcode(modify_input(intcode_from_file, noun, verb))
            if result[0] == DESIRED_OUTPUT:
                return [noun, verb]

noun_and_verb = naive_search()

print(extract_answer(noun_and_verb))
