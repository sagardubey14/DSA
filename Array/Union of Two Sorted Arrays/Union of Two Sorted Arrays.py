a = [1,2,3,4,5,6,7,8,9,10]
b = [2,3,4,4,5,11,12]

freq={}
union = []
for i in a:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] =1

for i in b:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] =1

for key in freq:
    union.append(key)

union.sort()

print(union)


def twoPointer(arr1,arr2,result):
    n1 = len(arr1)
    n2 = len(arr2)
    a = arr1
    b = arr2
    i = 0
    j=0
    while(i<n1 and j<n2):
        if a[i]<=b[j]:
            if len(result)==0 or result[-1] != a[i]:
                result.append(a[i])
            i+=1
        else:
            if len(result)==0 or result[-1] !=b[j]:
                result.append(b[j])
            j+=1

    while i<n1:
        if result[-1] != a[i]:
            result.append(a[i])
        i+=1
    while j<n2:
        if result[-1] != b[j]:
            result.append(b[j])
        j+=1
    print(result)

twoPointer(a,b,[])



