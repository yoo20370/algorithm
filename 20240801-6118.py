# N, M = list(map(int , input().split()))

# graph = [ [] for i in range(N+1)] 

# for _ in range(M) :
#     first, second = list(map(int, input().split()))
#     graph[first].append(second)
#     graph[second].append(first)

# visited = [ False for i in range(N+1)]
# minCost = [ 0 for i in range(N+1)]

# max = 0
# for i in range(1, N+1) :
#     for j in graph[i] :
#         if minCost[i] > minCost[j] + 1 or minCost[i] == 0:
#             minCost[i] = minCost[j] + 1
#             if max < minCost[i] :
#                 max = minCost[i]

# result = 0
# if minCost.count(max) != 1 :
#     for i in range(N+1) :
#         if minCost[i] == max :
#             result = i 
#             break

# print(result, max, minCost.count(max))

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


queue = deque([1])
visited = [-1] * (N+1)
visited[1] = 0
    
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if visited[neighbor] == -1:
            visited[neighbor] = visited[current] + 1
            queue.append(neighbor)
    
maxCost = max(visited)
first_maxNum = visited.index(maxCost)
count = visited.count(maxCost)
    
print(first_maxNum, maxCost, count)



