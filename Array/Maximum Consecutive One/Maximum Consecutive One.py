inp = [1, 1, 0, 1, 1, 1]
# output = 3

def findMax(arr):
    maxie = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count +=1
        if arr[i] == 0 or i == len(arr)-1:
            maxie = max(maxie,count)
            count = 0
    return maxie

print(findMax(inp))

