import sys
from functools import lru_cache

@lru_cache(None)
def modified_ackermann(a,b,c):

    while a > 0:
        if b == 0:
            b = c
        else:
            b = modified_ackermann(a,b-1,c)
        a -= 1
    
    return (b+1)%32768
    
@lru_cache(None)
def ackermann(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1,1)
    return ackermann(m-1, ackermann(m, n-1))


if __name__ == "__main__":
    sys.setrecursionlimit(30000)
    print(modified_ackermann(4,1,1))
