raw_input_base = """"""

raw_input_full = """"""


raw_input = raw_input_full

stones = [int(stone) for stone in raw_input.split(' ')]


def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  
        else:
            flat_list.append(item)
    return flat_list


# print(stones)

def evolve(stone : int): 
    if stone == 0: 
        return [1] 
    elif len(str(stone)) % 2 == 0: 
        stone = str(stone)
        x = len(stone) // 2
        return [int(stone[:x]), int(stone[x:])]
    else: 
        return [stone * 2024]
    
def puzzle_1(stones : list[int]): 

    def step(stones : list[int]): 
        res = []
        for stone in stones: 
            for evolved_stone in evolve(stone): 
                res.append(evolved_stone)
        
        return res 

    for i in range(25): 
       stones = step(stones)

    return len(stones)


# end part 1 

# part 2 needs to not be brute force 
# let's memoize in some way 

d = {}
for stone in stones: 
    d[stone] = d.get(stone, 0) + 1


def puzzle_2(stones : dict[int, int]): 

    def step(stones : dict[int, int]): 
        res = {}
        for stone, freq in stones.items(): 
            for evolved_stone in evolve(stone): 
                res[evolved_stone] = res.get(evolved_stone, 0) + freq
        
        return res 
    
    for i in range(75): 
       print(f'step {i}')
       stones = step(stones)

    
    return sum([val for val in list(stones.values())])

print(puzzle_2(d))