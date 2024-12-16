import heapq

raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

board = [[elt for elt in row] for row in raw_input.split('\n')]

# so, we're actually going to turn this into a 3D space and then dijkstra ]
# where i, j, k = board[i][j] at a certain direction k 
# each node then (i, j, k) is adjacent to (i + k0, j + k1, k) at distance 1 and (i, j, next k) at distance 1000 
# provided there are no walls 

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

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_legal_neighbors(i, j, direction_idx, m, n, board): 
    res = []
    direction = directions[direction_idx]
    new_i, new_j = i + direction[0], j + direction[1]
    if i >= 0 and j >= 0 and i < m and j < n and board[i][j] != '#':
        res.append(((new_i, new_j, direction_idx), 1))
    
    res.append(((i, j, (direction_idx + 1) % len(directions)), 1000))
    res.append(((i, j, (direction_idx - 1) % len(directions)), 1000))
    return res


def puzzle1(board): 
    m = len(board)
    n = len(board[0])
    
    q = []
    SFMap = {}
    visited = set()

    start = find_starting_posn(board)
    target = find_target_posn(board)

    q.append((0, (start[0], start[1], 0)))

    # dijkstra! 
    # we will be using a heap for the queue 
    # don't need backpointers 

    while q: 
        d, (curr_i, curr_j, curr_direction_idx) = heapq.heappop(q)

        if (curr_i, curr_j) == target: 
            return d 
        
        if (curr_i, curr_j, curr_direction_idx) in visited: 
            continue 

        visited.add((curr_i, curr_j, curr_direction_idx))
        nbrs = find_legal_neighbors(curr_i, curr_j, curr_direction_idx, m, n, board)
        for (nbr_i, nbr_j, nbr_direction), dist in nbrs: 
            if (nbr_i, nbr_j, nbr_direction) not in SFMap: 
                SFMap[(nbr_i, nbr_j, nbr_direction)] = dist + d 
            else: 
                SFMap[(nbr_i, nbr_j, nbr_direction)] = min(dist + d, SFMap[(nbr_i, nbr_j, nbr_direction)])
            
            heapq.heappush(q, ((SFMap[(nbr_i, nbr_j, nbr_direction)]), (nbr_i, nbr_j, nbr_direction)))

    
    return -1



# puzzle 2 is just the same but keeping track of backpointers huh.
# OK i guess! 
# oops, it needs ALL shortest paths huh. so I need to make backpointers be able to point to multiple nodes when there is equality of distance 

def debug_output(board, nodes): 
    m = len(board)
    n = len(board[0])
    for i in range(m): 
        row = [] 
        for j in range(n): 
            if (i, j) in nodes: 
                row.append('O')
            else: 
                row.append(board[i][j])
        print(''.join(row))

def pathify(node, bkptrs): 
    curr = node
    nodes = set() 
    # nodes.add(curr)

    def pathify_aux(curr): 
        nonlocal nodes 
        if curr == None: 
            return 
        nodes.add(curr)
        if bkptrs[curr] == None:
            return
        for bkptr in bkptrs[curr]: 
            pathify_aux(bkptr)


    pathify_aux(curr)

    res = set(map(lambda x : (x[0], x[1]), list(nodes)))

    debug_output(board, res)   
    return len(res)

def puzzle2(board): 
    m = len(board)
    n = len(board[0])
    
    q = []
    SFMap = {}
    visited = set()
    bkptrs = {}

    start = find_starting_posn(board)
    target = find_target_posn(board)

    q.append((0, (start[0], start[1], 0)))
    SFMap[(start[0], start[1], 0)] = 0
    bkptrs[(start[0], start[1], 0)] = None

    # dijkstra, but keep track of all shortest paths instead of just one

    while q: 
        d, (curr_i, curr_j, curr_direction_idx) = heapq.heappop(q)

        if (curr_i, curr_j) == target: 
            return pathify((curr_i, curr_j, curr_direction_idx), bkptrs)

        
        if (curr_i, curr_j, curr_direction_idx) in visited: 
            continue 

        visited.add((curr_i, curr_j, curr_direction_idx))
        nbrs = find_legal_neighbors(curr_i, curr_j, curr_direction_idx, m, n, board)
        for (nbr_i, nbr_j, nbr_direction), dist in nbrs: 
            if (nbr_i, nbr_j, nbr_direction) not in SFMap: 
                SFMap[(nbr_i, nbr_j, nbr_direction)] = dist + d 
                bkptrs[(nbr_i, nbr_j, nbr_direction)] = [(curr_i, curr_j, curr_direction_idx)]
            else: 
                # here we can check if they are equal or strictly less, and change bkptrs accordingly
                if dist + d < SFMap[(nbr_i, nbr_j, nbr_direction)]: 
                    SFMap[(nbr_i, nbr_j, nbr_direction)] = dist + d
                    bkptrs[(nbr_i, nbr_j, nbr_direction)] = [(curr_i, curr_j, curr_direction_idx)]
                if dist + d == SFMap[(nbr_i, nbr_j, nbr_direction)]: 
                    bkptrs[(nbr_i, nbr_j, nbr_direction)] = bkptrs.get((nbr_i, nbr_j, nbr_direction), []) + [(curr_i, curr_j, curr_direction_idx)]
            
            heapq.heappush(q, ((SFMap[(nbr_i, nbr_j, nbr_direction)]), (nbr_i, nbr_j, nbr_direction)))

    
    return -1

