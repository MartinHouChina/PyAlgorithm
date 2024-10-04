import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, Tuple, TypeVar, Optional
T = TypeVar('T')

class SortedSet(Generic[T]):
    BLOCK_SIZE = 16
    SPLIT_RATIO = 24
    
    def __init__(self, data: Iterable[T] = [], duplicate_allowed=False) -> None:
        
        if not duplicate_allowed:
            data = set(data)

        data = list(data)
        data.sort()

        self.size = len(data)
        block_cnt = int(math.ceil(math.sqrt(self.size / self.BLOCK_SIZE)))

        self.duplicate_allowed = duplicate_allowed
        self.data = [data[self.size * i // block_cnt : self.size * (i + 1) // block_cnt] for i in range(block_cnt)]

    def __iter__(self) -> Iterator[T]:
        for block in self.data:
            for ele in block: yield ele

    def __reversed__(self) -> Iterator[T]:
        for block in reversed(self.data):
            for ele in reversed(block): yield ele

    def __contains__(self, x):
        bidx, idx = self.lower_bound(x)
        if bidx == len(self.data) or idx == len(self.data[bidx]): return False
        return self.data[bidx][idx] == x
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.data)
    
    def prev(self, bidx, idx):
        if idx == 0:
            return bidx - 1, len(self.data[bidx - 1]) - 1
        else:
            return bidx, idx - 1

    def next(self, bidx, idx):
        if idx + 1 == len(self.data[bidx]):
            return bidx + 1, 0
        else: 
            return bidx, idx + 1

    def insert(self, x: T):
        if self.size == 0:
            self.data.append([x])
            self.size += 1
            return 
        
        if x > self.data[-1][-1]:
            self.size += 1
            if len(self.data) <= math.sqrt(self.size):
                self.data.append([x])
            else:
                self.data[-1].append(x)
            return 
        
        bidx, idx = self.lower_bound(x)
        if not self.duplicate_allowed and x in self: return

        self.data[bidx].insert(idx, x)
        self.size += 1

        if len(self.data[bidx]) > len(self.data) * self.SPLIT_RATIO:
            mid = len(self.data[bidx]) >> 1
            self.data[bidx: bidx + 1] = [self.data[bidx][: mid], self.data[bidx][mid: ]]

    def _find_block_that_contains_left(self, x: T):
        if self.size == 0 or self.data[-1][-1] < x:
            return len(self.data)
        L, R = 0, len(self.data) - 1
        while L < R:
            mid = (L + R) >> 1
            if self.data[mid][-1] >= x: R = mid
            else: L = mid + 1
        return L
    
    def _find_block_that_contains_right(self, x: T):
        if self.size == 0 or self.data[-1][-1] < x:
            return len(self.data)
        L, R = 0, len(self.data) - 1
        while L < R:
            mid = (L + R) >> 1
            if self.data[mid][-1] <= x: L = mid + 1
            else: R = mid
        return L
    
    def min(self) -> T:
        return self.data[0][0]
    
    def max(self) -> T:
        return self.data[-1][-1]

    def lower_bound(self, x: T) -> Tuple[int, int]:
        bidx = self._find_block_that_contains_left(x)
        if bidx == len(self.data): return bidx, 0
        return bidx, bisect_left(self.data[bidx], x)

    def upper_bound(self, x: T) -> Tuple[int, int]:
        bidx = self._find_block_that_contains(x)
        if bidx == len(self.data): return bidx, 0
        return bidx, bisect_right(self.data[bidx], x)

    def remove(self, bidx, idx):
        self.data[bidx].pop(idx)
        self.size -= 1
        if not self.data[bidx]:
            self.data.pop(bidx)

    def erase(self, x: T):
        L_bidx, L_idx = self.lower_bound(x)
        R_bidx, R_idx = self.upper_bound(x)
        if L_bidx == R_bidx:
            for _ in range(R_idx - L_idx):
                self.data[L_bidx].pop(L_idx)
                self.size -= 1
            if not self.data[L_bidx]:
                self.data.pop(L_bidx)
        else:
            for _ in range(len(self.data[L_bidx]) - L_idx):
                self.data[L_bidx].pop[L_idx]
                self.size -= 1
            
            for _ in range(R_idx):
                self.data[R_bidx].pop[0]
                self.size -= 1
            
            for _ in range((R_bidx if R_bidx is not None else len(self.data)) - (L_bidx + 1)):
                self.size -= len(self.data[L_bidx + 1])
                self.data.pop(L_bidx + 1)

            if not self.data[L_bidx]:
                self.data.pop(L_bidx)

    def is_begin(self, bidx, idx):
        return bidx == 0 and idx == 0
    
    def is_end(self, bidx, idx):
        return bidx == len(self.data) and idx == 0

    def get(self, bidx, idx):
        return self.data[bidx][idx]
    


Q = int(input())
S = SortedSet(duplicate_allowed=True)
from sortedcontainers import SortedList



A = SortedList([])

# for _ in range(Q):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         x = query[1]
        
#     elif query[0] == 2:
#         x, k = query[1:]
#         idx = A.bisect_right(x)
#         if idx - k < 0:
#             print(-1)
#         else:
#             print(A[idx - k])
#     elif query[0] == 3:
#         x, k = query[1:]
#         idx = A.bisect_left(x)
#         if idx + k - 1 >= len(A):
#             print(-1)
#         else:
#             print(A[idx + k - 1])


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        S.insert(q[1])
        A.add(q[1])
    elif q[0] == 3:
        # x, k = q[1:]
        # idx = A.bisect_left(x)
        # if idx + k - 1 >= len(A):
        #     print(-1)
        # else:
        #     print(A[idx + k - 1])
        flag = True
        pos = S.lower_bound(q[1])
        if S.is_end(*pos):
            print(-1)
            continue 
        for _ in range(q[2] - 1):
            if S.is_end(*S.next(*pos)):
                flag = False 
                break
            pos = S.next(*pos)
        if flag: print(S.get(*pos))
        else: print(-1)
    else:
        x, k = q[1:]
        idx = A.bisect_right(x)
        if idx - k < 0:
            print(-1)
        else:
            print(A[idx - k])
        # flag = True
        # pos = S.upper_bound(q[1])
        # for i in range(q[2]):
        #     if S.is_begin(*pos):
        #         flag = False 
        #         break
        #     pos = S.prev(*pos)
        # if flag and pos[0] >= 0: print(S.get(*pos))
        # else: print(-1)