raw_input_base = """""" # removing per advent guidelines

raw_input_full = """""" # removing per advent guidelines

raw_input = raw_input_full

raw_input = raw_input.split('\n')
for i, row in enumerate(raw_input): 
    raw_input[i] = [letter for letter in row]

m = len(raw_input)
n = len(raw_input[0])

target_string = 'XMAS'

#clockwise from top left
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def puzzle_1(letters : list[list[str]]) -> int: 
    count = 0 

    def puzzle_1_aux(i, j, curr_string, path, direction):
        nonlocal count 
        if curr_string == target_string: 
            count += 1
            return 
    
        target_letter = target_string[len(curr_string)]

        delY, delX = direction 
        new_i, new_j = i + delY, j + delX
        if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n: 
            if letters[new_i][new_j] == target_letter: 
                puzzle_1_aux(new_i, new_j, curr_string[:] + target_letter, path + [(new_i, new_j)], direction)

    for i in range(m): 
        for j in range(n): 
            if letters[i][j] == 'X': 
                for direction in directions: 
                    puzzle_1_aux(i, j, 'X', [(i, j)], direction)

    return count


# print(puzzle_1(raw_input))

# END part 1

# begin part 2
# basically we need to look for A's, and then it has to have corners like 
# MMSS, SSMM, MSMS, SMSM
# in this format its top left, top right, bottom left, bottom right
# so we can stringify the corners for every A, and then count 

def puzzle_2(letters : list[list[str]]) -> int: 
    count = 0 

    def getCorners(i : int, j : int) -> str: 
        res = ''
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for direction in directions: 
            delY, delX = direction 
            new_i, new_j = i + delY, j + delX
            if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n: 
                res += letters[new_i][new_j]
            else: 
                res += '.'
        return res

    for i in range(m):
        for j in range(n): 
            if letters[i][j] == 'A': 
                corners = getCorners(i, j)
                if corners in ['MSMS', 'MMSS', 'SSMM', 'SMSM']: 
                    count +=1

    return count

# print(puzzle_2(raw_input))