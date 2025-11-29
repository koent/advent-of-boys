from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
def diff(source_1, source_2):
    return sum(char_1 == char_2 for char_1, char_2 in zip(source_1, source_2))

def overlap(source_1,source_2):
    #return set(source_1)&set(source_2)
    for char_1,char_2 in zip(source_1,source_2):
        if char_1 == char_2:
            yield char_1
from itertools import combinations

for source_1,source_2 in combinations(data,2):
    if diff(source_1,source_2):
        break
    
print(''.join(overlap(source_1,source_2)))