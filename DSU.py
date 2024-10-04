class DSU:
    def __init__(self, n: int) -> None:
        self.fa = list(range(n))
        self.sz = [1] * n
    
    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def merge(self, a, b):
        A, B = self.find(a), self.find(b)
        if A != B:
            self.fa[B] = A
            self.sz[A] += self.sz[B]

    def same(self, a, b):
        return self.find(a) == self.find(b)
        
