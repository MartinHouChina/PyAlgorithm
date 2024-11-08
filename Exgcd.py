from typing import Tuple

def exgcd(a, b) -> Tuple[int, int, int]:
    if b == 0: return (a, 1, 0)
    g, x, y = exgcd(b, a % b)
    return (g, y, x - a / b * y)