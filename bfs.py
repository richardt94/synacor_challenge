from collections import deque

symbols = [["22","-", "9", "*" ],
           ["+", "4", "-", "18"],
           ["4", "*", "11","*" ],
           ["*", "8", "-", "1" ]]


def bfs(tgt_weight):
    q = deque()
    q.append((0,0,symbols[0][0],int(symbols[0][0])))

    m = len(symbols)
    n = len(symbols[0])

    while True:
        x, y, path, weight = q.popleft()

        if x == n-1 and y == m-1:
            if weight == tgt_weight:
                return path
            else:
                continue

        for xn, yn in ((x+1,y), (x,y+1), (x-1,y), (x,y-1)):
            if xn < 0 or xn >= n or yn < 0 or yn >= m:
                continue
            if xn == 0 and yn == 0: #do not pass go twice
                continue
            nsymb = symbols[yn][xn]
            nweight = weight
            if nsymb.isdigit():
                am = int(nsymb)
                op = path[-1]
                if op == "+":
                    nweight += am
                elif op == "*":
                    nweight *= am
                elif op == "-":
                    nweight -= am
                else:
                    raise ValueError("passed two numbers in a row")
            npath = path + nsymb
            q.append((xn,yn,npath,nweight))
    return path

if __name__ == "__main__":
    print(bfs(30))