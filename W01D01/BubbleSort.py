def bubbleSort(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

list1 = [8,3,-2,99,-44]

bubbleSort(list1)

print(list1)
                
