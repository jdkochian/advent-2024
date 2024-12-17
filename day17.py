import re 

raw_input_base = """Register A: 130504279429904
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

raw_input_full = """Register A: 7
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,4,5,0,3,5,5,3,0"""

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

    return 

puzzle_1(registers, program)
