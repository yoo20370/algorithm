import copy
from collections import deque 

N, M = list(map(int, input().split()))

inputList = [[] for _ in range(N)]

for i in range(N) :
    inputData = list(map(int, input().split()))
    for j in inputData :
        inputList[i].append(j)

# 북, 남, 서, 동
locations = [(0,-1), (0,1), (-1,0), (1,0)]

def findStartPosition(N,M,map) :
     for i in range(1, N-1) :
        for j in range(1, M-1) :
            if map[i][j] != 0 :
                startP = (i, j)
                return startP

def bfs(N, M, map):
    visited = [[False for _ in range(M)] for _ in range(N)]
    x, y = findStartPosition(N, M, map)
    queue = deque([(x, y)])
    visited[x][y] = True 
    cnt = 1 
    
    while queue:
        currX, currY = queue.popleft()
        for dx, dy in locations:
            nextX, nextY = currX + dx, currY + dy
            if 0 <= nextX < N and 0 <= nextY < M and not visited[nextX][nextY] and map[nextX][nextY] != 0:
                queue.append((nextX, nextY))
                visited[nextX][nextY] = True
                cnt += 1
    return cnt

def meltOneYear(N, M, map) :
    afterMap = copy.deepcopy(map)
    remainCnt = 0
    for i in range(1, M-1) :
        for j in range(1, N-1) :
            if map[j][i] != 0 :
                cnt = 0
                for x, y in locations :
                    if map[j + y][i + x] == 0 :
                        cnt += 1
                afterMap[j][i] -= cnt
                if afterMap[j][i] < 0 :
                    afterMap[j][i] = 0
                if afterMap[j][i] != 0 :
                    remainCnt += 1
    return afterMap, remainCnt

year = 0 
while True :
    year += 1
    inputList, cnt = meltOneYear(N, M, inputList)
    ccnt = bfs(N,M,inputList)
    if  cnt != ccnt :
        print(year)
        break
    if cnt == 0 or ccnt == 0:
        print(0)