import re 
import heapq

raw_input_base=""""""

raw_input_full = """"""

raw_input = raw_input_full

pattern = r"p=(\d+),(\d+)\s*v=(-?\d+),(-?\d+)"

matches = re.findall(pattern, raw_input)
robots = [] 
for match in matches: 
    x_0, y_0, v_x, v_y = map(int, match)
    robots.append({'p0': (y_0, x_0), 'v': (v_y, v_x)})

# test_robot = robots[4]
#  we use modulo here? 

COLOR_RESET = "\033[0m"
COLOR_ANTINODE = "\033[1;32m" # green
def debug_output(m, n, posns): 
    board = [[' ' for _ in range(n)] for _ in range(m)]
    for (y, x), v in posns.items(): 
        board[y][x] = f"{COLOR_ANTINODE}{str(v)}{COLOR_RESET}"

    for row in board: 
        print(''.join(row))


def puzzle_1(robots, m, n, _iter): 
    final_posns = {}

    for robot in robots: 
        del_y = (robot['v'][0] * _iter) % m
        del_x = (robot['v'][1] * _iter) % n
        y_1, x_1 = ((robot['p0'][0] + del_y) % m, (robot['p0'][1] + del_x) % n)
        final_posns[(y_1, x_1)] = final_posns.get((y_1, x_1), 0) + 1 

    debug_output(m, n, final_posns)

    q1, q2, q3, q4 = 0, 0, 0, 0
    for (y, x), count in final_posns.items():
        if y < m // 2 and x < n // 2: 
            q1 += count 
        elif y < m // 2 and x > n // 2: 
            q2 += count 
        elif y > m // 2 and x < n // 2: 
            q3 += count 
        elif y > m // 2 and x > n // 2: 
            q4 += count 

    
    print(final_posns)
    return q1 * q2 * q3 * q4



# print(puzzle_1(robots, 7, 11, 100))
# print(puzzle_1(robots, 103, 101, 100))


# new plan: just check every safety score and look at the interesting ones for the tree

def puzzle_2(robots, m, n): 
    final_safety_scores = []
    for i in range(10000):
        safety_score = puzzle_1(robots, m, n, i)
        # sort by safety score
        heapq.heappush(final_safety_scores, (safety_score, i))

    print(final_safety_scores)
    return 
