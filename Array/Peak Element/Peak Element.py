arr = [1, 1, 1]

def findPeak():
    for i in range(len(arr)):
        print(i)
        if i ==0:
            if arr[i]>=arr[i+1]:
                return i
        if i == len(arr)-1:
            if arr[i-1]<=arr[i]:
                return i
        if arr[i-1]<=arr[i]>=arr[i+1]:
            return i
    return -1

print(findPeak())