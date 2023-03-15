def mergeSort(list1):
    if len(list1) > 1:

        r = len(list1)//2
        L = list1[:r]
        M = list1[r:]

        mergeSort(L)
        mergeSort(M)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                list1[k] = L[i]
                i += 1
            else:
                list1[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            list1[k] = L[i]
            i += 1
            k += 1
        
        while j < len(M):
            list1[k] = M[j]
            j += 1
            k += 1

list1 = [8,3,-2,99,-44]
mergeSort(list1)

print(list1)