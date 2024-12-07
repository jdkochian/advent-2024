raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

raw_input = raw_input.split('\n')
for i, level in enumerate(raw_input): 
    target, operands = level.split(':')
    operands = [int(num) for num in operands.strip().split(' ')]
    target = int(target)
    raw_input[i] = (target, operands)

def evaluate(curr, target, operands, operands_idx, operation, operands_length, concatenate_allowed=False): 
    # base case: all operands done
    if operands_idx == operands_length: 
        return curr == target
    
    next_num = operands[operands_idx]
    if operation == '+': 
        curr = curr + next_num 
    elif operation == '*': 
        curr = curr * next_num 
    elif operation == '||': 
        curr = int(str(curr) + str(next_num))
    
    # recursive step
    if concatenate_allowed: 
        concatenate_eval = evaluate(curr, target, operands, operands_idx + 1, '||', operands_length, concatenate_allowed)
    else: 
        concatenate_eval = False
    return evaluate(curr, target, operands, operands_idx + 1, '+', operands_length, concatenate_allowed) or evaluate(curr, target, operands, operands_idx + 1, '*', operands_length, concatenate_allowed) or concatenate_eval


def puzzle_1(levels : list[tuple[int, list[int]]]): 
    res = 0 
    for level in levels: 
        target, operands = level 
        if evaluate(0, target, operands, 0, '+', len(operands)): 
            res += target
    
    return res 

def puzzle_2(levels : list[tuple[int, list[int]]]): 
    res = 0 
    for level in levels: 
        target, operands = level 
        if evaluate(0, target, operands, 0, '+', len(operands), True): 
            res += target
    
    return res 

