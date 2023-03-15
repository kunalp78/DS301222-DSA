def selectionSort(list1):

    for step in range(len(list1)):
        min = step
        for i in range(step+1, len(list1)):
            if list1[i] < list1[min]:
                min = i

        list1[step], list1[min] = list1[min], list1[step]

list1 = [8,3,-2,99,-44]
selectionSort(list1)
print(list1)