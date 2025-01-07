arr = [7, 10, 4, 20,15]
k = 4
maxar = [float('inf')]*k
l=0
r = 5
for i in range(l,r):
    if arr[i]<maxar[0]:
        j=k-1
        while j>0:
            print(maxar,arr[i])
            maxar[j]=maxar[j-1]
            j-=1
        maxar[0] = arr[i]

print(maxar[k-1])