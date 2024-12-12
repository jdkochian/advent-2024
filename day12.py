raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full
raw_input = [[elt for elt in row] for row in raw_input.split("\n")]

def findAreaPerimiterOfRegionRec(i, j, m, n, board, visited):
    a = 0 
    p = 0 

    curr = board[i][j]

    def visit(i, j):
        nonlocal visited 
        nonlocal a
        nonlocal p
        if (i, j) in visited: 
            return

        visited.add((i, j))

        a += 1
        for delY, delX in [(0, -1), (-1, 0), (1, 0), (0, 1)]: 
            new_y, new_x = i + delY, j + delX 
            if new_y >= 0 and new_x >= 0 and new_y < m and new_x < n: 
                if board[new_y][new_x] == curr: 
                    visit(new_y, new_x)
                else: 
                    p += 1
            else: 
                p += 1
    
    visit(i, j)

    return a, p


def puzzle_1(board : list[list[str]]): 
    _sum = 0 
    visited = set() 

    m = len(board)
    n = len(board[0])

    for i in range(m): 
        for j in range(n): 
            if (i, j) not in visited: 
                a, p = findAreaPerimiterOfRegionRec(i, j, m, n, board, visited)
                _sum += a * p

    return _sum 

# print(puzzle_1(raw_input))

# end pizzle 1 
# begin puzzle 2 

# we know that the number of sides of a polygon is the number of corners, so let's count corners 
# for each given node, it can be a corner in four directions 
# for each of those directions, (tl, tr, bl, br), it has a bunch of states where it is a corner, exmaples with tl: 
# 1) both t and l are the same, and tl diagonal is not 
# 2) both t and l are not the same as it
# 3) one of t or l is not the same and one of t or l is out of bounds 
# 4) both t and l are out of bounds 

# so with the three vars vert neighbnor, horiz neighbor, diagonal neighbor, this is the state breakdown, wehere T means it is in bounds and same region and F otherwise: 

# is corner: TTF, FFT, FFF

# is not corner: TTT, TFT, FTT, TFF, FTF

# this handles double counting because we don't count TFT or FTT (?)

def getNumCorners(i, j, m, n, board, curr): 
    d = {} 
    _sum = 0 

    for direction, delY, delX in [('l', 0, -1), ('t', -1, 0), ('b', 1, 0), ('r', 0, 1), ('tl', -1, -1), ('tr', -1, 1), ('bl', 1, -1), ('br', 1, 1)]:
        new_y, new_x = i + delY, j + delX
        if new_y >= 0 and new_x >= 0 and new_y < m and new_x < n: 
            if board[new_y][new_x] == curr: 
                d[direction] = 'T'
            else: 
                d[direction] = 'F'
        else: 
            d[direction] = 'F'
    
    for vert_nbr, horiz_nbr, diag_nbr in [('t', 'l', 'tl'), ('t', 'r', 'tr'), ('b', 'l', 'bl'), ('b', 'r', 'br')]: 
        s = ""
        s += d[vert_nbr] + d[horiz_nbr] + d[diag_nbr]
        if s in ['TTF', 'FFT', 'FFF']: 
            _sum += 1
    
    # print(i, j, _sum)
    return _sum 



def findAreaSidesOfRegionRec(i, j, m, n, board, visited): 
    a = 0 
    corners = 0 
    # we know that num sides = num corners 
    curr = board[i][j]

    def visit(i, j):
        nonlocal visited 
        nonlocal a
        nonlocal corners
        if (i, j) in visited: 
            return

        visited.add((i, j))

        a += 1
        corners += getNumCorners(i, j, m, n, board, curr)
        for delY, delX in [(0, -1), (-1, 0), (1, 0), (0, 1)]: 
            new_y, new_x = i + delY, j + delX 
            if new_y >= 0 and new_x >= 0 and new_y < m and new_x < n: 
                if board[new_y][new_x] == curr: 
                    visit(new_y, new_x)
    visit(i, j)

    return a, corners


def puzzle_2(board : list[list[str]]): 
    _sum = 0 
    visited = set() 

    m = len(board)
    n = len(board[0])

    for i in range(m): 
        for j in range(n): 
            if (i, j) not in visited: 
                a, sides = findAreaSidesOfRegionRec(i, j, m, n, board, visited)
                print(board[i][j], a, sides)
                _sum += a * sides
                # print(_sum)

    return _sum 


print(puzzle_2(raw_input))