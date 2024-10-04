class FenNode:
    def __init__(self, value = 0) -> None:
        self.value = value

    @staticmethod
    def identity():
        return FenNode(0)

    def __add__(self, other):
        return FenNode(self.value + other.value)
    
    def __iadd__(self, other):
        self = self + other
        return self
    
    def __repr__(self) -> str:
        return f"FenNode({self.value})"
    

class Fenwick:
    def __init__(self, N: int) -> None:
        self.N = N
        self.tr = [FenNode.identity()] * N
    
    def add(self, pos: int, value: FenNode):
        pos += 1
        while pos <= self.N:
            self.tr[pos - 1] += value
            pos += pos & (-pos)
    
    def query(self, pos: int):
        res = FenNode.identity()
        while pos > 0:
            res += self.tr[pos - 1]
            pos -= pos & (-pos)
        return res

    def __repr__(self) -> str:
        repr = "Fenwick(["
        for i in range(self.N):
            repr += self.query(i).__repr__() + (", " if i + 1 != self.N else "")
        repr += "])"
        return repr
