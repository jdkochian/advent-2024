raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

pairs = []

for pair in raw_input.split("\n"): 
    j, i = map(int, pair.split(','))
    pairs.append((i, j))

def getLegalNeighbors(i, j, m, n): 
    res = []
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
        new_i, new_j = i + direction[0], j + direction[1]
        if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n: 
            res.append((new_i, new_j))
    return res 

def puzzle_1(pairs : list[tuple[int]], m : int, n : int, num_simulated : int): 
    board = [['.' for _ in range(n)] for _ in range(m)]
    target = (m - 1, n - 1)
    start = (0, 0)
    for i in range(num_simulated): 
        corrupted_i, corrupted_j = pairs[i]
        board[corrupted_i][corrupted_j] = '#'

    # we can bfs now i guess, since costs are uniform 
    q = [(0, start)]
    visited = set() 

    while q: 
        cost, curr = q.pop(0)
        curr_i, curr_j = curr 

        if curr == target: 
            return cost 

        if curr in visited: 
            continue 
            
        visited.add(curr)
        for nbr_i, nbr_j in getLegalNeighbors(curr_i, curr_j, m, n): 
            if board[nbr_i][nbr_j] != '#': 
                q.append((cost + 1, (nbr_i, nbr_j)))

    return -1


def puzzle_2(pairs : list[tuple[int]], m: int, n : int, start_simulating: int): 
    board = [['.' for _ in range(n)] for _ in range(m)]
    target = (m - 1, n - 1)
    start = (0, 0)
    for i in range(start_simulating): 
        corrupted_i, corrupted_j = pairs[i]
        board[corrupted_i][corrupted_j] = '#'

    def is_reachable(): 
        q = [start]
        visited = set() 
        while q: 
            curr = q.pop(0)
            curr_i, curr_j = curr 

            if curr == target: 
                return True 

            if curr in visited: 
                continue 

            visited.add(curr)
            for nbr_i, nbr_j in getLegalNeighbors(curr_i, curr_j, m, n): 
                if board[nbr_i][nbr_j] != '#': 
                    q.append((nbr_i, nbr_j))

        return False 
    
    for i in range(start_simulating, len(pairs)): 
        pair_to_add = pairs[i]
        corrupted_i, corrupted_j = pair_to_add
        board[corrupted_i][corrupted_j] = '#'
        print(f'testing corrupting byte {i}')
        if not is_reachable(): 
            return corrupted_i, corrupted_j
        

print(puzzle_2(pairs, 71, 71, 1024))