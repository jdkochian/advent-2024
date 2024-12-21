raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

towels, designs = raw_input.split('\n\n')
towels =[elt.strip() for elt in towels.split(',')] 
designs = designs.split('\n')

def is_possible(towels, design): 
    # A[i] = solution for design[0:i]
    # leetcode  
    # A[i] = any(design[0:j] in towels, design[j : i] in towels) fpr all j such that A[j] is true?
    # let's give it a shot but this seems slow 

    A = [False] * (len(design) + 1)

    for i in range(1, len(design) + 1): 
        if design[0:i] in towels: 
            A[i] = True
            continue
        for j in range(i): 
            if A[j] == True:
                if design[j:i] in towels: 
                    A[i] = True
    
    return A[-1]

# print(towels)
# print(designs)

def puzzle_1(towels, designs): 
    _sum = 0 
    for design in designs: 
        if is_possible(towels, design): 
            _sum += 1

    return _sum 

# print(puzzle_1(towels, designs))

# for part 2, we can do the same thing just count ways instead of booleans 

def get_num_ways(towels, design): 
    # A[i] = solution for design[0:i]
    # A[i] = sum(design[0:j] in towels, design[j : i] in towels) for all j <= i 

    A = [0] * (len(design) + 1)
    for i in range(1, len(design) + 1): 
        if design[0:i] in towels: 
            A[i] += 1 
        for j in range(i):
            if design[j:i] in towels:
                A[i] += A[j]

    return A[-1]

def puzzle_2(towels, designs): 
    _sum = 0 
    for design in designs:
        _sum += get_num_ways(towels, design)

    return _sum

print(puzzle_2(towels, designs))