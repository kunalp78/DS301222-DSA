def linearSearch(list1, value):
    for i in range(len(list1)):
        if list1[i] == value:
            return i
    return -1

l = [5, 0, -1, 99, 2, 3]
index = linearSearch(l, -1)
if index == -1:
    print("Element not found!!")
else:
    print(index ,l[index])