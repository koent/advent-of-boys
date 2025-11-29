from collections import defaultdict
from itertools import combinations
from pathlib import Path
import re

from tqdm import tqdm

# Read the input
with open(Path(__file__).parent / Path('test_input.txt'), 'r') as f:
    lines = f.read().splitlines()
    
class Solution:
    
    def __init__(self, lines: list[str]):
        self.input = self.parse_input(lines)
        self.max_x, self.max_y = self._get_max_coordinates()
        # self.grid_count = self._count_hits()
        
        
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
    
    def _get_max_coordinates(self): 
        max_x = 0
        max_y = 0
        
        for request in self.input:
            # Look at the x-coordinate
            max_x = max(max_x, self.input[request][1][0])
            # Look at the y-coordinate
            max_y = max(max_y, self.input[request][1][1])
        return max_x, max_y
    
    def _count_hits(self):
        """For each point in the grid, lookn how many times it appears in a request"""
        coordinate_count = defaultdict(int)
        for i in tqdm(range(self.max_x), ascii=True, desc="Counting hits..."):
            for j in range(self.max_y):
                for request in self.input:
                    # Check if the coordinate falls within the request
                    if self.input[request][0][0]<=i<self.input[request][1][0] and self.input[request][0][1]<=j<self.input[request][1][1]:
                        coordinate_count[(i,j)]+=1
                        
        return coordinate_count    
    
    def visualize(self):
        for j in range(self.max_y+1):  
            for i in range(self.max_x+1):
                if (i,j) in self.grid_count.keys():
                    print(self.grid_count[(i,j)], end="")
                else:
                    print(".", end="")
            print()
            
    def _check_for_overlap(r_1,r_2):
        x_0 = max(r_1[0][0], r_2[0][0])
        x_1 = min(r_1[1][0], r_2[1][0])
        if x_0>x_1:
            return False
            
        
        y_0 = max(r_1[0][1], r_2[0][1])
        y_1 = min(r_1[1][1], r_2[1][1])
        if y_0>y_1:
            return False
        
        return True
            
    def answer(self):
        for id_1 in self.input:
            for id_2 in self.input:
                self._check_for_overlap()
                
                
if __name__ == "__main__":
    solution = Solution(lines) 
    print(solution.answer())