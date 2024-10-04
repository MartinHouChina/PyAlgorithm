from typing import List
from bisect import bisect_left

class Discretization:
    def __init__(self, data: List[int]) -> None:
        self.content = list(set(data))
        self.content.sort()
    
    def getRank(self, val: int):
        return bisect_left(self.content, val)
    
    def getKth(self, idx: int):
        return self.content[idx]