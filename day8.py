import time
import os

# Define ANSI color codes
COLOR_RESET = "\033[0m"
COLOR_HASH = "\033[1;31m"  # Bright Red for general '#'
COLOR_NODE = "\033[1;34m"  # Bright Blue for nodes (letters)
COLOR_DOT = "\033[1;30m"   # Gray for '.'
COLOR_P1_P2 = "\033[1;31m" # Bright Red for `p1` and `p2`
COLOR_ANTINODE = "\033[1;32m" # Bright Green for the antinode

raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_base

raw_input = raw_input.split('\n')

for i, level in enumerate(raw_input): 
    raw_input[i] = [elt for elt in level]



def find_antinodes(p1, p2, m, n): 
    # calcualte the manhattan distance between two nodes, and then go that distance from each and check if in bounds
    p1_y, p1_x = p1
    p2_y, p2_x = p2

    delY = p2_y - p1_y 
    delX = p2_x - p1_x

    res = []

    for possible_antinode in [(p2_y + delY, p2_x + delX), (p2_y - delY, p2_x - delX), (p1_y + delY, p1_x + delX), (p1_y - delY, p1_x - delX)]:
        if possible_antinode == p1 or possible_antinode == p2:
            continue 
        if possible_antinode[0] >= 0 and possible_antinode[1] >= 0 and possible_antinode[0] < m and possible_antinode[1] < n: 
            res.append(possible_antinode)

    return res

def puzzle1(board : list[list[str]]): 
    m = len(board)
    n = len(board[0])

    antinodes = set()

    d = {} 
    for i in range(m): 
        for j in range(n): 
            if board[i][j] != '.': 
                d[board[i][j]] = d.get(board[i][j], []) + [(i, j)]
    

    for k, v in d.items(): 
        lst = v
        for i in range(len(lst)): 
            for j in range(i + 1, len(lst)): 
                res = find_antinodes(lst[i], lst[j], m, n)
                for antinode in res: 
                    antinodes.add(antinode)


    # print(d)
    return len(antinodes)


# print(puzzle1(raw_input))

def find_antinodes_p2(p1, p2, m, n): 
    # calcualte the manhattan distance between two nodes, and then iterate from each node in both directions until out of bounds
    p1_y, p1_x = p1
    p2_y, p2_x = p2

    delY = p2_y - p1_y 
    delX = p2_x - p1_x

    res = []

    # for possible_antinode in [(p2_y + delY, p2_x + delX), (p2_y - delY, p2_x - delX), (p1_y + delY, p1_x + delX), (p1_y - delY, p1_x - delX)]:
    #     if possible_antinode[0] >= 0 and possible_antinode[1] >= 0 and possible_antinode[0] < m and possible_antinode[1] < n: 
    #         res.append(possible_antinode)

    for node in [p1, p2]: 
        for direction in [(1, 1), (-1, -1)]: 
            possible_antinode = node 
            while possible_antinode[0] >= 0 and possible_antinode[1] >= 0 and possible_antinode[0] < m and possible_antinode[1] < n: 
                res.append(possible_antinode)
                possible_antinode = (possible_antinode[0] + (delY * direction[0]), possible_antinode[1] + (delX * direction[1]))

    return res

def puzzle2(board : list[list[str]]): 
    m = len(board)
    n = len(board[0])

    antinodes = set()

    d = {} 
    for i in range(m): 
        for j in range(n): 
            if board[i][j] != '.': 
                d[board[i][j]] = d.get(board[i][j], []) + [(i, j)]
    

    for k, v in d.items(): 
        lst = v
        for i in range(len(lst)): 
            for j in range(i + 1, len(lst)): 
                res = find_antinodes_p2(lst[i], lst[j], m, n)
                for antinode in res: 
                    antinodes.add(antinode)


    # print(d)
    return len(antinodes)


def find_antinodes_anim(p1, p2, m, n): 
    # calcualte the manhattan distance between two nodes, and then go that distance from each and check if in bounds
    p1_y, p1_x = p1
    p2_y, p2_x = p2

    delY = p2_y - p1_y 
    delX = p2_x - p1_x

    res = []

    for possible_antinode in [(p2_y + delY, p2_x + delX), (p2_y - delY, p2_x - delX), (p1_y + delY, p1_x + delX), (p1_y - delY, p1_x - delX)]:
        if possible_antinode == p1 or possible_antinode == p2:
            continue 
        if possible_antinode[0] >= 0 and possible_antinode[1] >= 0 and possible_antinode[0] < m and possible_antinode[1] < n: 
            res.append((p1, p2, possible_antinode))

    return res

def pretty_print(board: list[list[str]], step): 
    p1, p2, antinode = step
    for i, row in enumerate(board): 
        colored_row = []
        for j, token in enumerate(row): 
            if (i, j) == p1 or (i, j) == p2: 
                colored_row.append(f"{"\033[1;34m"}{token}{COLOR_RESET}")
            elif (i, j) == antinode: 
                colored_row.append(f"{COLOR_ANTINODE}{token}{COLOR_RESET}")
            else: 
                colored_row.append(token)
        print(' '.join(colored_row))
    print('-----')


def puzzle_1_anim(board : list[list[str]]): 
    m = len(board)
    n = len(board[0])
    anim_board = board[:]

    antinodes = set()

    d = {} 
    for i in range(m): 
        for j in range(n): 
            if board[i][j] != '.': 
                d[board[i][j]] = d.get(board[i][j], []) + [(i, j)]
    
    animation_steps = []


    for k, v in d.items(): 
        lst = v
        for i in range(len(lst)): 
            for j in range(i + 1, len(lst)): 
                res = find_antinodes_anim(lst[i], lst[j], m, n)
                for step in res: 
                    animation_steps.append(step)


    def animate(board : list[list[str]], steps):
        for step in steps: 
            os.system('cls' if os.name == 'nt' else 'clear')
            p1, p2, antinode = step 
            board[antinode[0]][antinode[1]] = '#'

            pretty_print(board, step)
            time.sleep(1)

    animate(anim_board, animation_steps)


    return len(antinodes)



# puzzle_1_anim(raw_input)