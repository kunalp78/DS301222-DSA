def binarySearch(list1, value):
    low = 0
    high = len(list1)-1
    while low <= high:
        mid = (low + high)//2

        if list1[mid] == value:
            return mid
        elif list1[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

l = [-1, 0, 2, 3, 5, 99]
index = binarySearch(l, -1)
if index == -1:
    print("Element not found!!")
else:
    print(index ,l[index])