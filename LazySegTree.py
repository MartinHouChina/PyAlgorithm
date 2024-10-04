from typing import List

class Tag:
    def __init__(self, opr: int) -> None:
        self.opr = opr

    @staticmethod
    def identity():
        return Tag(0)

    def __add__(self, other):
        return Tag(self.opr + other.opr)
    
    def __iadd__(self, other):
        self = self + other
        return self

    def __repr__(self) -> str:
        return f"Tag({self.opr})"



class LazyNode:
    def __init__(self, value = 0, length = 0) -> None:
        self.value = value
        self.length = length

    @staticmethod
    def identity():
        return LazyNode(0, 0)

    def __add__(self, other):
        return LazyNode(self.value + other.value, self.length + other.length)
    
    def __iadd__(self, other):
        self = self + other
        return self
    
    def apply(self, t: Tag):
        self.value += t.opr * self.length
    
    def __repr__(self) -> str:
        return f"LazyNode({self.value, self.length})"
    


class LazyTree:
    def __init__(self, L, R) -> None:
        self.tr: List[LazyNode] = [LazyNode.identity()]
        self.tag: List[Tag] = [Tag.identity()]
        self.L_child: List[int] = [None]
        self.R_child: List[int] = [None]
        self.parent: List[int] = [None]
        self.L = L 
        self.R = R
    
    def _init(self, idx, pidx, dir):
        if pidx is not None:
            if dir == 0:                    
                self.L_child[pidx] = len(self.tr)
            else:
                self.R_child[pidx] = len(self.tr)
                    
        idx = len(self.tr)
        self.tr.append(LazyNode.identity())
        self.parent.append(pidx)
        self.L_child.append(None)
        self.R_child.append(None)
        self.tag.append(Tag.identity())
        return idx

    def _down(self, idx):
        l, r = self.L_child[idx], self.R_child[idx]
        t = self.tag[idx]

        if l is None:
            l = self._init(l, idx, 0)
        
        if r is None:
            r = self._init(r, idx, 1)

        self.tr[l].apply(t)
        self.tag[l] += t

        self.tr[r].apply(t)
        self.tag[r] += t

        self.tag[idx] = Tag.identity() 

    def _up(self, idx):
        childl = LazyNode.identity() if self.L_child[idx] is None else self.tr[self.L_child[idx]]
        childr = LazyNode.identity() if self.R_child[idx] is None else self.tr[self.R_child[idx]]
        self.tr[idx] = childl + childr

    def updateRange(self, l: int, r: int, t: Tag, L: int = None, R: int = None, nodeIdx: int = 0, parentIdx: int = None, dir: int = None):
        
        if L is None:
            L = self.L

        if R is None:
            R = self.R

        if nodeIdx is None:
            nodeIdx = self._init(nodeIdx, parentIdx, dir)

        if R < l or r < L:
            return
                
        if l <= L and R <= r:
            self.tr[nodeIdx].apply(t)
            self.tag[nodeIdx] += t
            return 
        
        mid = (L + R) >> 1
        
        self._down(nodeIdx)
        self.updateRange(l, r, t, L, mid, self.L_child[nodeIdx], nodeIdx, 0)
        self.updateRange(l, r, t, mid + 1, R, self.R_child[nodeIdx], nodeIdx, 1)
        self._up(nodeIdx)
        
    
    def updatePos(self, pos: int, node: LazyNode, L: int = None, R: int = None, nodeIdx: int = 0, parentIdx: int = None, dir: int = None):
        
        if L is None:
            L = self.L

        if R is None:
            R = self.R

        if nodeIdx is None:
            nodeIdx = self._init(nodeIdx, parentIdx, dir)

        if L == R:
            self.tr[nodeIdx] = node
            return 
        
        mid = (L + R) >> 1
        self._down(nodeIdx)
        if pos <= mid: self.updatePos(pos, node, L, mid, self.L_child[nodeIdx], nodeIdx, 0)
        else: self.updatePos(pos, node, mid + 1, R, self.R_child[nodeIdx], nodeIdx, 1)
        self._up(nodeIdx)
    
    def query(self, l: int, r: int, L: int = None, R: int = None, nodeIdx: int = 0):
        
        if L is None:
            L = self.L 
        
        if R is None:
            R = self.R
        
        if R < l or r < L:
            return LazyNode.identity()

        if l <= L and R <= r:
            return self.tr[nodeIdx]

        mid = (L + R) >> 1
        self._down(nodeIdx)
        res = self.query(l, r, L, mid, self.L_child[nodeIdx]) + self.query(l, r, mid + 1, R, self.R_child[nodeIdx]) 
        return res
    
    def __repr__(self) -> str:
        return f"SegTree({str(self.tr)} | {str(self.tag)})"



if __name__ == '__main__':
    tree = LazyTree(1, 4)
    
    A = [1, 3, 1, 4]
    
    for i in range(len(A)):
        tree.updatePos(i + 1, LazyNode(A[i], 1))


    print(tree)

    tree.updateRange(1, 3, Tag(2))
    tree.updatePos(2, LazyNode(-100, 2))
    
    print(tree)
    print(tree)
    print(tree)