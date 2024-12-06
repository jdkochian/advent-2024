import sys

raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

# could I have done iterative? yes. should I have done iterative? also yes. am I stubborn? also yes.
sys.setrecursionlimit(10000)

raw_input = raw_input.split("\n")
for i in range(len(raw_input)): 
    raw_input[i] = [elt for elt in raw_input[i]]

def find_starting_posn(board : list[list[str]]): 
    for i in range(len(board)): 
        for j in range(len(board[i])): 
            if board[i][j] == '^': 
                return (i, j)
            


def puzzle_1(board : list[list[str]]) -> int: 
    start_i, start_j = find_starting_posn(board)
    visited = set() 
    m = len(board)
    n = len(board[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # can't do it recursively... did I hit an infinite loop somewhere? 
    # let's write a new function that 
    def visit(i, j, board, direction_idx): 
        nonlocal visited
        # 3 cases: 
        # just a . or an X, make it an X and keep going 
        # a #, turn and visit 
        # if outside, return 
        direction = directions[direction_idx]
        # print(i, j)
        if i < 0 or j < 0 or i >= m or j >= n: 
            return
        elif board[i][j] == '.' or board[i][j] == 'X' or board[i][j] == '^': 
            board[i][j] = 'X'
            visited.add((i, j))
            visit(i + direction[0], j + direction[1], board, direction_idx)
        elif board[i][j] == '#': 
            # we have to turn right FROM the index before this one 
            prev_i, prev_j = i - direction[0], j - direction[1]
            direction_idx = (direction_idx + 1) % len(directions)
            direction = directions[direction_idx]
            visit(prev_i + direction[0], prev_j + direction[1], board, direction_idx)

    visit(start_i, start_j, board, 0)

    return len(visited)


m = len(raw_input)
n = len(raw_input[0])


def puzzle_2(board : list[list[str]], placed_obstacle) -> bool: 
    start_i, start_j = find_starting_posn(board)
    tmp = board[placed_obstacle[0]][placed_obstacle[1]]
    board[placed_obstacle[0]][placed_obstacle[1]] = '0'
    # print(board)
    visited = set() 
    m = len(board)
    n = len(board[0])


    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]   
    def visit(i, j, board, direction_idx): 
        nonlocal visited
        # if in visited at this direction, we are in a loop so return 
        if ((i, j, direction_idx)) in visited: 
            return True
        
        visited.add((i, j, direction_idx))

        # 3 cases: 
        # just a . or an X, make it an X and keep going 
        # a # or 0, turn and visit 
        # if outside, return 
        direction = directions[direction_idx]
        if i < 0 or j < 0 or i >= m or j >= n: 
            return False
        elif board[i][j] == '.' or board[i][j] == 'X' or board[i][j] == '^': 
            visited.add((i, j, direction_idx))
            return visit(i + direction[0], j + direction[1], board, direction_idx)
        elif board[i][j] == '#' or board[i][j] == '0': 
            # we have to turn right FROM the index before this one 
            prev_i, prev_j = i - direction[0], j - direction[1]
            direction_idx = (direction_idx + 1) % len(directions)
            direction = directions[direction_idx]
            return visit(prev_i + direction[0], prev_j + direction[1], board, direction_idx)

    res = visit(start_i, start_j, board, 0)
    board[placed_obstacle[0]][placed_obstacle[1]] = tmp
    return res


# print(puzzle_2(raw_input, (6, 3)))
_sum = 0

for i in range(m): 
    for j in range(n): 
        if raw_input[i][j] != '#':
            print(f'checking {i, j}')
            if puzzle_2(raw_input, (i, j)): 
                _sum += 1

print(_sum)