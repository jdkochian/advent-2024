import heapq
raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full


board = [[elt for elt in row] for row in raw_input.split('\n')]


def find_char_in_board(char : str, board):
    m = len(board)
    n = len(board[0])

    for i in range(m): 
        for j in range(n): 
            if board[i][j] == char: 
                return (i, j)
            
def find_starting_posn(board):
    return find_char_in_board('S', board)

def find_target_posn(board): 
    return find_char_in_board('E', board)


def getLegalNeighbors(i, j, m, n): 
    res = []
    for delY, delX in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_Y, new_X = i + delY, j + delX 
        if new_Y >= 0 and new_X >= 0 and new_Y < m and new_X < n: 
            res.append((new_Y, new_X))
    return res 

# basically, you can turn a # to . as long as you can end up on a ., and we have to find the shortest path for all possible versions of that 

def get_shortest_path_length(board, start, target, cheat_start, cheat_end): 
    visited = set() 
    frontier = []
    m = len(board)
    n = len(board[0])

    start_Y, start_X = start

    frontier.append((0, (start_Y, start_X)))
    while frontier: 
        cost, curr = heapq.heappop(frontier)

        if curr in visited: 
            continue

        if curr == target: 
            return cost 
        
        visited.add(curr)
        if curr == cheat_start: 
            heapq.heappush(frontier, (cost + 1, (cheat_end[0], cheat_end[1])))
        else:
            for nbr in getLegalNeighbors(curr[0], curr[1], m, n): 
                if board[nbr[0]][nbr[1]] != '#' or nbr == cheat_start: 
                    heapq.heappush(frontier, (cost + 1, (nbr[0], nbr[1])))

    return -1 


def puzzle_1(board): 
    m = len(board)
    n = len(board[0])

    start = find_starting_posn(board)
    target = find_target_posn(board)

    start_end_set = set() 

    save_counts = {} 

    baseline_cost = get_shortest_path_length(board, start, target, (-1, -1), (-1, -1))

    for i in range(m): 
        for j in range(n): 
            start_cheat = (i, j)

            if board[start_cheat[0]][start_cheat[1]] == '#': 
                for nbr in getLegalNeighbors(i, j, m, n): 
                    if board[nbr[0]][nbr[1]] == '.' or board[nbr[0]][nbr[1]] == 'E' and (i, j, nbr[0], nbr[1]) not in start_end_set: 
                        start_end_set.add((i, j, nbr[0], nbr[1]))
                        cost = get_shortest_path_length(board, start, target, (i, j), (nbr[0], nbr[1]))
                        if cost != baseline_cost:
                            save_counts[baseline_cost - cost] = save_counts.get(baseline_cost - cost, 0) + 1
                            print((start_cheat[0], start_cheat[1], nbr[0], nbr[1], baseline_cost - cost))

    count = 0
    for k, v in save_counts.items(): 
        if k >= 100: 
            count += v
    return count 


# puzzle_1(board)





