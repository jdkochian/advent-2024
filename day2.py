# commented out per advent guidelines
raw_input_base = """"""

raw_input_full =""""""


raw_input = raw_input_full

levels = raw_input.split('\n')
levels = [list(map(lambda x : int(x), level.split(' '))) for level in levels]

def is_increasing_within_range(level: list[int]) -> bool: 
    for i in range(len(level)): 
        if i == 0: 
            continue
        # check if this is smaller than prev elt (diff less than 0) or out of range 
        diff = level[i] - level[i - 1]
        if diff <= 0 or diff > 3:
            return False 
    return True

def is_decreasing_within_range(level: list[int]) -> bool: 
    for i in range(len(level)): 
        if i == 0: 
            continue 
        # check if this is larger than prev elt (diff greater than 0) or out of range
        diff = level[i - 1] - level[i]
        if diff <= 0 or diff > 3:
            return False 
    return True  


def is_safe_level(level : list[int]) -> bool: 
    return is_decreasing_within_range(level) or is_increasing_within_range(level)



def puzzle_1(levels: list[list[int]]):
    _sum = 0 
    for level in levels: 
        if is_safe_level(level): 
            _sum += 1
    return _sum


# END puzzle 1 
def puzzle_2(levels: list[list[int]]): 
    _sum = 0 
    for level in levels: 
        if is_safe_level(level): 
            _sum += 1
        else: 
            for i in range(len(level)): 
                tmp = level.pop(i)
                dampened_is_safe = is_safe_level(level)
                if dampened_is_safe: 
                    _sum += 1
                    break 
                level.insert(i, tmp)

    return _sum

print(puzzle_2(levels))
