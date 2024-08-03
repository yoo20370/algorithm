from collections import deque

# 테스트 케이스 입력 
T = int(input())


def algFunc() :
    inputList = []
    
    # 맥주를 파는 편의점의 개수 
    N = int(input())

    # 좌표 입력 
    for _ in range(N+2) :
        x, y = list(map(int ,input().split()))
        
        inputList.append( [x, y] )
    # 방문 처리
    visited = [ False for _ in range(N+2)] 
    
    queue = deque([0]) 
    visited[0] = True
    
    while queue :
        curr = queue.popleft()
        if curr == N + 1 : 
            return 'happy'
        
        for next in range(N+2) :
            currX, currY = inputList[curr] 
            x, y = inputList[next]
            if not visited[next] and abs(currX - x) +abs(currY - y) <= 1000 :
                visited[next] = True
                queue.append(next)

    return 'sad'

for _ in range(T) :
    print(algFunc())
