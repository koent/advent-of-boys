from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    
def contains_multiple(source,  multiple = 2):
    counts = Counter(source)
    return multiple in counts.values()

amount_of_doubles = sum(contains_multiple(source,2) for source in data) 
amount_of_triples = sum(contains_multiple(source,3) for source in data) 

print(amount_of_doubles * amount_of_triples)
