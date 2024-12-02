from collections import Counter

raw_input = """""" # removing input per guidelines
list1 = []
list2 = []

pairs = raw_input.split('\n')
for pair in pairs: 
    pair = list(filter(lambda x : x != '', pair.split(' ')))
    list1.append(int(pair[0]))
    list2.append(int(pair[1]))


def puzzle_1(l1 : list[int], l2 : list[int]) -> int: 
    l1 = sorted(l1)
    l2 = sorted(l2)
    _sum = 0 
    for i in range(len(l1)): 
        _sum += abs(l1[i] - l2[i])
    
    return _sum 


def puzzle_2(l1 : list[int], l2: list[int]) -> int: 
    l2_freq = Counter(l2)
    similarity_score = 0
    for num in l1: 
        if num in l2_freq: 
            similarity_score += num * l2_freq[num]
        
    return similarity_score


