from pathlib import Path
import re

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
    
    @staticmethod
    def _check_for_overlap(r_1,r_2):
        x_0 = max(r_1[0][0], r_2[0][0])
        x_1 = min(r_1[1][0], r_2[1][0])
        if x_0>=x_1:
            return False
            
        
        y_0 = max(r_1[0][1], r_2[0][1])
        y_1 = min(r_1[1][1], r_2[1][1])
        if y_0>=y_1:
            return False
        
        return True
            
    def answer(self):
        nonoverlapping = {}
        for id_1 in self.input:
            nonoverlapping[id_1]=True
            for id_2 in self.input:
                if id_1 != id_2 and self._check_for_overlap(self.input[id_1], self.input[id_2]):
                    nonoverlapping[id_1] = False
        
        # Return the id's that are nonioverlapping
        return [k for k,v in nonoverlapping.items() if v][0]
                
                
if __name__ == "__main__":
    solution = Solution(lines) 
    print(solution.answer())