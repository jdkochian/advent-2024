raw_input_base = """""" # removed per advent guidelines

raw_input_full = """""" # removed per advent guidelines

raw_input = raw_input_full

rules, updates = raw_input.split('\n\n')
 
rules = rules.split('\n')
updates = updates.split('\n')
updates = [update.split(',') for update in updates]


# I probably should have also done part 1 with in-degrees instead of out-degrees, but oh well. 


d = {}
for rule in rules: 
    # u must come before v, so let's make a mapping of v to u to check if anything after it should be before it 
    u, v = rule.split('|')
    d[u] = d.get(u, set()) | {v}


def is_update_legal(update : list[str], d) -> bool: 
    for i in range(len(update) - 1): 
        curr_set = d.get(update[i], set())
        for j in range(i + 1, len(update)): 
            if update[j] not in curr_set: 
                return False 
    return True

def puzzle1(updates : list[list[str]], d) -> int: 
    _sum = 0
    for update in updates: 
        print(update, is_update_legal(update, d))
        if is_update_legal(update, d): 
            _sum += int(update[len(update) // 2])

    return _sum


# END puzzle 1


# now we have to sort the ones that are incorrectly ordered. 
# we can topological sort, but indegrees are weird when there are nodes that are not taken into account 
# if I could remake d such that it only included relevant nodes, then it would be totally doable to just sort by in-degree

in_d ={}
for rule in rules: 
    u, v = rule.split('|')
    in_d.setdefault(v, set()).add(u)
    in_d.setdefault(u, set())


def fix_illegal_update(update : list[str], d) -> str: 
    relevant_nodes = set()
    relevant_d = d.copy()

    res = []

    for item in update: 
        relevant_nodes.add(item)

    # get in-degree only including nodes that are in this update 
    for k, v in d.items(): 
        if k not in relevant_nodes: 
            del relevant_d[k]
        else: 
            relevant_d[k] = relevant_nodes.intersection(v)


    # sort by in-degree
    res = sorted(update, key = lambda x : len(relevant_d[x]))
    return res 

def puzzle2(updates : list[list[str]], d, in_d) -> int: 
    _sum = 0
    for update in updates: 
        if not is_update_legal(update, d): 
            fixed = fix_illegal_update(update, in_d)
            _sum += int(fixed[len(fixed) // 2])

    return _sum

# print(puzzle2(updates, d, in_d))