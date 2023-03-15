def insertionSort(list1):
    for i in range(1,len(list1)):
        key = list1[i]
        j = i-1
        while j>=0 and list1[j] > key:
            list1[j+1] = list1[j]
            j = j-1
        list1[j+1] = key

list1 = [8,3,-2,99,-44]

insertionSort(list1)

print(list1)