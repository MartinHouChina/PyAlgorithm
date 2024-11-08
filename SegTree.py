from typing import List


class SegNode:
    def __init__(self, value = 0) -> None:
        self.value = value

    @staticmethod
    def identity():
        return SegNode(0)

    def __add__(self, other):
        return SegNode(self.value + other.value)
    
    def __iadd__(self, other):
        self = self + other
        return self
    
    def __repr__(self) -> str:
        return f"SegNode({self.value})"
    


class SegTree:
    def __init__(self, L, R) -> None:
        self.tr: List[SegNode] = [SegNode.identity()]
        self.L_child: List[int] = [None]
        self.R_child: List[int] = [None]
        self.L = L 
        self.R = R
    
    def updateSet(self, pos: int, node: SegNode, L: int = None, R: int = None, nodeIdx: int = 0, parentIdx: int = None, dir: int = None):
        
        if L is None:
            L = self.L

        if R is None:
            R = self.R

        if nodeIdx is None:

            if parentIdx is not None:
                if dir == 0:                    
                    self.L_child[parentIdx] = len(self.tr)
                else:
                    self.R_child[parentIdx] = len(self.tr)
                    
            nodeIdx = len(self.tr)
            self.tr.append(SegNode.identity())
            self.L_child.append(None)
            self.R_child.append(None)


        if L == R:
            self.tr[nodeIdx] = node
            return 
        
        mid = (L + R) >> 1
        if pos <= mid: self.update(pos, node, L, mid, self.L_child[nodeIdx], nodeIdx, 0)
        else: self.update(pos, node, mid + 1, R, self.R_child[nodeIdx], nodeIdx, 1)

        childl = SegNode.identity() if self.L_child[nodeIdx] is None else self.tr[self.L_child[nodeIdx]]
        childr = SegNode.identity() if self.R_child[nodeIdx] is None else self.tr[self.R_child[nodeIdx]]

        self.tr[nodeIdx] = childl + childr

    def updateAdd(self, pos: int, node: SegNode, L: int = None, R: int = None, nodeIdx: int = 0, parentIdx: int = None, dir: int = None):
        
        if L is None:
            L = self.L

        if R is None:
            R = self.R

        if nodeIdx is None:

            if parentIdx is not None:
                if dir == 0:                    
                    self.L_child[parentIdx] = len(self.tr)
                else:
                    self.R_child[parentIdx] = len(self.tr)
                    
            nodeIdx = len(self.tr)
            self.tr.append(SegNode.identity())
            self.L_child.append(None)
            self.R_child.append(None)


        if L == R:
            self.tr[nodeIdx] += node
            return 
        
        mid = (L + R) >> 1
        if pos <= mid: self.update(pos, node, L, mid, self.L_child[nodeIdx], nodeIdx, 0)
        else: self.update(pos, node, mid + 1, R, self.R_child[nodeIdx], nodeIdx, 1)

        childl = SegNode.identity() if self.L_child[nodeIdx] is None else self.tr[self.L_child[nodeIdx]]
        childr = SegNode.identity() if self.R_child[nodeIdx] is None else self.tr[self.R_child[nodeIdx]]

        self.tr[nodeIdx] = childl + childr
    
    def query(self, l: int, r: int, L: int = None, R: int = None, nodeIdx: int = 0):
        
        if nodeIdx is None:
            return SegNode.identity()

        if L is None:
            L = self.L   
        
        if R is None:
            R = self.R
        
        if R < l or r < L:
            return SegNode.identity()

        if l <= L and R <= r:
            return self.tr[nodeIdx]

        mid = (L + R) >> 1
        res = self.query(l, r, L, mid, self.L_child[nodeIdx]) + self.query(l, r, mid + 1, R, self.R_child[nodeIdx]) 
        return res
    
    def __repr__(self) -> str:
        return f"SegTree({str(self.tr)})"


