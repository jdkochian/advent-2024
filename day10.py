raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full

raw_input = raw_input.split('\n')
for i, row in enumerate(raw_input): 
    raw_input[i] = [int(token) for token in row]


def getLegalNeighbors(i, j, m, n): 
    res = [] 
    for delY, delX in [(0, -1), (-1, 0), (1, 0), (0, 1)]: 
        new_y, new_x = i + delY, j + delX
        if new_y >= 0 and new_x >= 0 and new_y < m and new_x < n: 
            res.append((new_y, new_x))

    return res

def getScoreOfTrailhead(i, j, m, n, board): 
    visited = set() 

    def visit(i, j, curr): 
        nonlocal visited 
        if curr == 9: 
            visited.add((i, j))
            return 

        for nbr_Y, nbr_X in getLegalNeighbors(i, j, m, n):
            if board[nbr_Y][nbr_X] == curr + 1: 
                visit(nbr_Y, nbr_X, curr + 1)


    
    # this has been called on a cell of 0, so we can visit 0 
    visit(i, j, 0)
    return len(visited)


def puzzle_1(board : list[list[int]]): 
    _sum = 0 

    m = len(board) 
    n = len(board[0])


    for i in range(m): 
        for j in range(n): 
            if board[i][j] == 0: 
                _sum += getScoreOfTrailhead(i, j, m, n, board)

    return _sum 

# can combine parts 1 and 2 but I like them being distinct 

def getRatingOfTrailhead(i, j, m, n, board): 
    rating = 0 
    def visit(i, j, curr): 
        nonlocal rating 
        if curr == 9: 
            rating += 1
            return 
        
        for nbr_Y, nbr_X in getLegalNeighbors(i, j, m, n):
            if board[nbr_Y][nbr_X] == curr + 1: 
                visit(nbr_Y, nbr_X, curr + 1)
    
    visit(i, j, 0)
    return rating 

def puzzle_2(board : list[list[int]]): 
    _sum = 0 
    m = len(board)
    n = len(board[0])

    for i in range(m): 
        for j in range(n): 
            if board[i][j] == 0: 
                _sum += getRatingOfTrailhead(i, j, m, n, board)
    
    return _sum 

print(puzzle_2(raw_input))