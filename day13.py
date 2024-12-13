import re
from sympy import symbols, Eq, solve

raw_input_base = """"""

raw_input_full = """"""

raw_input = raw_input_full


pattern = r"Button A: X\+(\d+),\s*Y\+(\d+)\nButton B: X\+(\d+),\s*Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

matches = re.findall(pattern, raw_input)

print(matches)

# let's use multidimensional dp to solve, shouldn't need the limit then bc itll be linear 
# nevermind! this is too slow! the limit was there to help on purpose! this code works though. 
def getLowestCostPossible(match : tuple[str]): 
    a_x, a_y, b_x, b_y, target_x, target_y = map(int, match) 
    dp = [[float('inf') for _ in range(target_x + 1)] for _ in range(target_y + 1)]
    dp[0][0] = 0 

    # iterate via the dp array 
    for i in range(target_y + 1): 
        for j in range(target_x + 1): 
            if i == 0 and j == 0: 
                continue
            # can we implement the limit here? 
            a_button_prev = dp[i - a_y][j - a_x] if i - a_y >= 0 and j - a_x >= 0 else float('inf')
            b_button_prev = dp[i - b_y][j - b_x] if i - b_y >= 0 and j - b_x >= 0 else float('inf')

            dp[i][j] = min(a_button_prev + 3, b_button_prev + 1)

    
    # print(dp)

    return dp[-1][-1]

# oh. it's a system of equations. two equations with two unknowns. i feel silly.

def getLowestCostPossibleUsingSysEq(match: tuple[str]): 
    a_x, a_y, b_x, b_y, target_x, target_y = map(int, match) 

    a, b = symbols('a b', integer=True)

    eq1 = Eq(a_x * a + b_x * b, target_x )
    eq2 = Eq(a_y * a + b_y * b, target_y)

    solution = solve((eq1, eq2), (a, b))

    if solution and solution[a] <= 100 and solution[b] <= 100: 
        return solution[a] * 3 + solution[b] * 1
    else: 
        return float('inf')


def getLowestCostPossibleUsingSysEqP2(match: tuple[str]): 
    a_x, a_y, b_x, b_y, target_x, target_y = map(int, match) 
    target_x, target_y = target_x + 10000000000000, target_y + 10000000000000

    a, b = symbols('a b', integer=True)

    eq1 = Eq(a_x * a + b_x * b, target_x )
    eq2 = Eq(a_y * a + b_y * b, target_y)

    solution = solve((eq1, eq2), (a, b))

    if solution: 
        return solution[a] * 3 + solution[b] * 1
    else: 
        return float('inf')


 

def puzzle_1(matches : list[tuple[str]]): 
    _sum = 0 
    for i, match in enumerate(matches): 
        print(f"Processing board {i}")
        cost = getLowestCostPossibleUsingSysEq(match)
        if cost != float('inf'): 
            _sum += cost 

    return _sum 

def puzzle_2(matches : list[tuple[str]]): 
    _sum = 0 
    for i, match in enumerate(matches): 
        print(f"Processing board {i}")
        cost = getLowestCostPossibleUsingSysEqP2(match)
        if cost != float('inf'): 
            _sum += cost 

    return _sum 

print(puzzle_2(matches))



