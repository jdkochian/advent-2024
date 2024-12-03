import re

raw_input_base = """""" # commenting out per advent guidelines

raw_input_full = """""" # commenting out per advent guidelines

raw_input = raw_input_full

pattern = r"mul\((\d+),(\d+)\)"

def puzzle_1(memory : str) -> int: 
    matches = re.findall(pattern, memory)
    res = 0
    for pair in matches: 
        res += int(pair[0]) * int(pair[1])

    return res


# print(puzzle_1(raw_input))

# END puzzle 1 

delimeters = r"(don't\(\)|do\(\))"

def puzzle_2(memory: str) -> int: 
    segments = re.split(delimeters, memory)
    res = 0
    do_mode = True
    for segment in segments: 
        if segment == "don't()": 
            do_mode = False 
            continue 
        elif segment == "do()": 
            do_mode = True 
            continue
        if do_mode: 
            res += puzzle_1(segment)

    return res


puzzle_2(raw_input)