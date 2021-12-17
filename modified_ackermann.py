import sys
from functools import lru_cache

@lru_cache(None)
def modified_ackermann(a,b,c):
    if a == 0:
        return (b+1)%32768
    if b == 0:
        return modified_ackermann(a-1,c,c)
    
    return modified_ackermann(a-1, modified_ackermann(a,b-1,c),c)

def ackermann(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1,1)
    return ackermann(m-1, ackermann(m, n-1))


if __name__ == "__main__":
    sys.setrecursionlimit(30000)
    print(ackermann(4,1))
