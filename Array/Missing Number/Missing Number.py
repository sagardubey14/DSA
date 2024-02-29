# Sample Input:
arr = [1, 2, 3, 5, 6, 7, 8]
# Sample Output : 4

def bruteForce():
    for i in range(1,len(arr)+1):
        present = 0
        for j in arr:
            if i == j:
                present = 1
            else:
                continue
        if present == 0:
            return i

print(bruteForce())

def hasMap():
    mp = [0]*(len(arr)+2)
    
    for i in arr:
        mp[i] += 1
    for i in range(1,len(arr)+1):
        if mp[i] == 0:
            return i

print(hasMap())

def smartWork():
    N = len(arr)+2
    finalSum = N*int((N-1)/2)
    sum = 0
    for i in arr:
        sum += i
    return (finalSum-sum)

print(smartWork())