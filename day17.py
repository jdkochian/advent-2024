import re 

raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

register_pattern =  r"Register\s*(?:A|B|C): (\d+)"

matches = re.findall(register_pattern, raw_input)

registers = [] 
for match in matches: 
    registers.append(int(match))

program_matches = re.findall(r"(\d+)", raw_input.split("\n\n")[1])
program = [] 
for num in program_matches: 
    program.append(int(num))



def puzzle_1(init_registers, program): 
    outputs = [] 
    isn_ptr = 0 
    halt_ptr = len(program)
    registers = init_registers

    def combo(operand): 
        if operand in [0, 1, 2, 3]: 
            return operand
        else: 
            return registers[operand - 4]

    while isn_ptr < halt_ptr: 
        opcode = program[isn_ptr]
        operand = program[isn_ptr + 1]
        if opcode == 0: 
            numerator = registers[0]
            denominator = 2 ** combo(operand)
            registers[0] = numerator // denominator 
            isn_ptr += 2
        elif opcode == 1: 
            registers[1] = registers[1] ^ operand 
            isn_ptr += 2
        elif opcode == 2: 
            registers[1] = combo(operand) % 8
            isn_ptr += 2 
        elif opcode == 3: 
            if registers[0] == 0 : 
                isn_ptr += 2 
            else: 
                isn_ptr = operand 
        elif opcode == 4: 
            registers[1] = registers[1] ^ registers[2]
            isn_ptr += 2
        elif opcode == 5: 
            outputs.append(combo(operand) % 8)
            isn_ptr += 2
        elif opcode == 6: 
            numerator = registers[0]
            denominator = 2 ** combo(operand)
            registers[1] = numerator // denominator 
            isn_ptr += 2
        elif opcode == 7: 
            numerator = registers[0]
            denominator = 2 ** combo(operand)
            registers[2] = numerator // denominator 
            isn_ptr += 2
        else: 
            print('uh oh!')

    print(','.join(map(str, outputs)))

    return outputs

puzzle_1(registers, program)

# ok, we need to copy the second program 

# register_value = 0
# for i in range(len(program) - 2, -1, -1): 
#     digit = program[i]
#     current_digit_iter = 0

#     outputs = puzzle_1([register_value, 0, 0], program)
#     while outputs[0] != digit and current_digit_iter < 8: 
#         register_value += 1
#         current_digit_iter += 1
#         # print(register_value)
#         outputs = puzzle_1([register_value, 0, 0], program)


#     # so then we multiply by 8 and go for the next one right? 
#     print(f'Moving to next digit at {register_value} which is {current_digit_iter} offset')
#     register_value = register_value * 8

# print(register_value)

# this literally works up until the last digit???

# ok so i think we can make this recursive to see if we can get it, what is happening above (I think) is that there are multiple times you can get the right digit 

def rec_puzzle_2(register_val, curr_offset, digit_to_test):
    outputs = puzzle_1([register_val, 0, 0], program)

    if outputs == [2, 4, 1, 1, 7, 5, 1, 5, 4, 5, 0, 3, 5, 5, 3, 0]: 
        print('I FOUND IT FINALLY', register_val)

    if program[digit_to_test] == outputs[0]: 
        print(outputs)
        for i in range(8): 
            rec_puzzle_2(register_val * 8 + i, i, digit_to_test - 1)
    else: 
        return 
    
for i in range(8): 
    rec_puzzle_2(i, 0, len(program) - 1)

