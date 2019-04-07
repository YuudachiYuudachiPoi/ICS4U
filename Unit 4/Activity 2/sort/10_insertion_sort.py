A = [3,5,7,2,3]
for j,key in enumerate(A):
    i = j
    while i != 0 and A[i-1] > key:
        A[i] = A[i-1]
        i -= 1
    A[i] = key 
print(A)