from collections import defaultdict
from itertools import combinations
from pathlib import Path
import re

from tqdm import tqdm

# Read the input
with open(Path(__file__).parent / Path('input.txt'), 'r') as f:
    lines = f.read().splitlines()
    
class Solution:
    
    def __init__(self, lines: list[str]):
        self.input = self.parse_input(lines)        
        
    @staticmethod        
    def parse_input(lines):
        """Convert the input to a dictionary"""
        requests = {}
        for line in lines:
            # Extract the id from the elf request
            id = int(re.findall(r"(?<=#)[0-9]*", line)[0])
            # Extract the coordinates from the elf request
            coordinates = [int(coor) for coor in re.findall(r"[0-9]+", line)[1:]]
            
            requests[id] = ((coordinates[0], coordinates[1]),(coordinates[0]+coordinates[2], coordinates[1]+coordinates[3]))
            
        return requests
            
    def answer(self):
        overlapping_squares = defaultdict(int)
        for id_1, id_2 in tqdm(combinations(self.input, 2), ascii=True, total = len(self.input)*(len(self.input)-1)//2):
            request_1=self.input[id_1]
            request_2=self.input[id_2]
            
            x_0 = max(request_1[0][0], request_2[0][0])
            x_1 = min(request_1[1][0], request_2[1][0])
            if x_0>x_1:
                continue
            
            y_0 = max(request_1[0][1], request_2[0][1])
            y_1 = min(request_1[1][1], request_2[1][1])
            if y_0>y_1:
                continue
            
            for i in range(x_0,x_1):
                for j in range(y_0,y_1):
                    overlapping_squares[(i,j)]+=1
                    
        return len(overlapping_squares)
            
            

if __name__ == "__main__":
    solution = Solution(lines) 
    print(solution.answer())