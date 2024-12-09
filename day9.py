raw_input_base = ''

raw_input_full = """"""

curr_id = 0
block = True 
filesystem = []

raw_input = raw_input_full

for elt in raw_input: 
    if block: 
        for i in range(int(elt)): 
            filesystem.append(str(curr_id))
        curr_id += 1
    else: 
        for i in range(int(elt)): 
            filesystem.append('.')
    block = not block 


def puzzle_1(filesystem : list[str]): 
    l = 0 
    r = len(filesystem) - 1
    while filesystem[r] == '.': 
        r -= 1
    while filesystem[l] != '.': 
        l += 1
    
    # precondition: first iter they are ready to swap 
    while l < r: 
        print(filesystem)
        filesystem[l] = filesystem[r]
        filesystem[r] = '.'
        while filesystem[r] == '.': 
            r -= 1
        while filesystem[l] != '.': 
            l += 1
    

    checksum = 0 
    for i, elt in enumerate(filesystem): 
        if elt == '.': 
            continue 
        checksum += i * int(elt)

    return checksum


# print(puzzle_1(filesystem))

# this will not work so great with strings, so let's use a list of tuples instead, now that data can't be broken up 


curr_id = 0
block = True 
filesystem = []

for elt in raw_input: 
    if block: 
        filesystem.append((curr_id, int(elt)))
        curr_id += 1
    else: 
        filesystem.append((-1, int(elt)))
    block = not block 



def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  
        else:
            flat_list.append(item)
    return flat_list

# for debugging 
def pretty_print(filesystem: list[str]): 
    res = ''
    for elt, size in filesystem:
        for i in range(size): 
            if elt == -1: 
                res += ('.')
            else: 
                res += (str(elt))
    
    print(res)
    return res


def flatten_fsm_tuples(filesystem : list[tuple[int, int]]): 
    res = []
    for elt, size in filesystem: 
        for i in range(size): 
            if elt == -1: 
                res.append(0)
            else: 
                res.append(elt)

    return res


# tried to write a better solution, gave up, back to O(n^2)

def puzzle_2(filesystem : list[str]): 
    l = 0 
    r = len(filesystem) - 1 

    while filesystem[r][0] == -1: 
        r -= 1
    
    while r > 0: 
        pretty_print(filesystem)
        l = 0 
        while l < r: 
            if filesystem[l][0] == -1 and filesystem[l][1] >= filesystem[r][1]: 
                # do the swap 

                _id, size = filesystem[r]
                free_space = filesystem[l][1]

                filesystem[r] = (-1, size)
                filesystem[l] = [(_id, size), (-1, free_space - size)]

                filesystem = flatten(filesystem)

                # break out of inner loop
                l = float('inf')
            else: 
                l += 1

        # move r to the next piece of data 
        r -= 1
        while filesystem[r][0] == -1: 
            r -= 1


    pretty_print(filesystem)
    filesystem = flatten_fsm_tuples(filesystem)
    checksum = 0 
    # empty space is 0's now, don't need a check
    for i, elt in enumerate(filesystem): 
        checksum += i * int(elt)
    return checksum