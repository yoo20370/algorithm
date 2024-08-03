# N = int(input())

# inputList = []
# for _ in range(N) :
#     inputList.append(list(map(int, input().split())))

# def algFunc(height, index) :
#     if height == N:
#         return 0
#     maxNum = max(algFunc(height+1, index), algFunc(height +1, index + 1))
#     return maxNum + inputList[height][index]

# print(algFunc(0,0))

N = int(input())

inputList = []
for _ in range(N) :
    inputList.append(list(map(int, input().split())))

n = 501
m = 502
dpTable = [[0]* m for _ in range(n)]

def algFunc(height, index) :
    if height == N :
        return 0
    if dpTable[height][index] != 0 :
        return dpTable[height][index]
    maxNum = max(algFunc(height+1, index), algFunc(height +1, index + 1))
    dpTable[height][index] = maxNum + inputList[height][index]
    return dpTable[height][index]

print(algFunc(0,0))