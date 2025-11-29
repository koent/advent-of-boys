from pathlib import Path

with open(Path(__file__).parent / Path('input.txt'), 'r') as f:
    print(sum(int(i) for i in f.readlines()))
