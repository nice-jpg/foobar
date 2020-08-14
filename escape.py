

m1 = [[0, 1, 1, 0], 
      [0, 0, 0, 1], 
      [1, 1, 0, 0], 
      [1, 1, 1, 0]]

m2 = [[0, 0, 0, 0, 0, 0], 
      [1, 1, 1, 1, 1, 0], 
      [0, 0, 0, 0, 0, 0], 
      [0, 1, 1, 1, 1, 1], 
      [0, 1, 1, 1, 1, 1], 
      [0, 0, 0, 0, 0, 0]]


m3 = [[0, 1, 1, 0], 
      [0, 0, 0, 1], 
      [1, 1, 0, 0], 
      [1, 1, 1, 0],
      [1, 0, 1, 0]]

m4 = [[0, 0, 0, 0, 1, 1],
      [0, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 1],
      [1, 0, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 1],
      [1, 1, 1, 0, 0, 0]]

def BFS(map):
    h = len(map)
    w = len(map[0])
    dis = [[float('inf') for _ in range(w)] for __ in range(h)]
    
    dis[0][0] = 1


    col = [0, 0, 1, -1]
    row = [1, -1, 0, 0]

    queue = []
    queue.append([0, 0])

    while queue:

        currentn = queue.pop(0)
        currentdis = dis[currentn[0]][currentn[1]]
        for i in range(4):
            ci = currentn[0] + col[i]
            ri = currentn[1] + row[i]
            isvalid = isValid(ci, ri, h, w)

            if isvalid and map[ci][ri]==0 and dis[ci][ri]==float('inf'):
                dis[ci][ri] = currentdis + 1
                queue.append([ci, ri])
    
    return dis[h-1][w-1]

def isValid(ci, ri, h, w):
    if ci < 0 or ri < 0:
        return False
    if ci >= h or ri >= w:
        return False
    return True

def solution(map):
    h = len(map)
    w = len(map[0])
    col = [0, 0, 1, -1]
    row = [1, -1, 0, 0]

    step = BFS(map)
    for ci in range(h):
        for ri in range(w):
            if map[ci][ri] == 0:
                continue
            
            ishcross = False
            isvcross = False

            if isValid(ci+col[0], ri+row[0], h, w) and isValid(ci+col[1], ri+row[1], h, w):
                isvcross = ((map[ci + col[0]][ri + row[0]] == 0) and (map[ci + col[1]][ri + row[1]] == 0))
            if isValid(ci+col[2], ri+row[2], h, w) and isValid(ci+col[3], ri+row[3], h, w):
                isvcross = ((map[ci + col[2]][ri + row[2]] == 0) and (map[ci + col[3]][ri + row[3]] == 0))
            if ishcross or isvcross:
                map[ci][ri] = 0
                t = BFS(map)
                step = min(t, step)
                map[ci][ri] = 1
    return step

    
print(solution(m2))