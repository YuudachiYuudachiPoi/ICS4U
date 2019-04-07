def merge(L,R):
    i,j = 0,0
    list = []
    for k in range(len(L) + len(R)):
        if len(R) != j and (len(L) == i or L[i] > R[j]):
            list.append(R[j])
            j += 1
        else:
            list.append(L[i])
            i += 1
    return list

def merge_sort(list):
    q = len(list)//2
    if q > 0:
        L = list[:q]
        R = list[q:]
        return merge(merge_sort(L),merge_sort(R))
    else:
        return list

A = [2,6,4,8,2,9,3,6,5,3,7,8,2,4,6,3,24,5,56,3,3,1,2]
print(merge_sort(A))

s = []
sorted()