def bucketSOrt(list1):

    bucket = []

    for i in range(len(list1)):
        bucket.append([])

    for j in list1:
        index = int(10 * j)
        bucket[index].append(j)
    
    for i in range(len(list1)):
        bucket[i] = sorted(bucket[i])
    
    k = 0
    for i in range(len(list1)):
        for j in range(len(bucket[i])):
            list1[k] = bucket[i][j]
            k += 1
    return list1

list1 = [.42, .32, .33, .52, .37, .47, .51]
print(bucketSOrt(list1))