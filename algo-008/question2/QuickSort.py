def qsort(array, mode):
    if len(array) < 2:
        return array, 0

    if mode == 2:
        array[0], array[-1] = array[-1], array[0]
    elif mode == 3:
        array = midian(array)
    array, i, j = part(array)

    array[: i], lans = qsort(array[: i], mode)
    array[i + 1 :], rans = qsort(array[i + 1 :], mode)

    return array, lans + rans + len(array) - 1

def part(array):
    pixot = array[0]
    i = 0
    j = 0
    for elem in array[1 :]:
        j += 1
        if elem < pixot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[0], array[i] = array[i], array[0]

    return array, i, j

def midian(array):
    firstele = array[0]
    middleele = array[(len(array) - 1) // 2]
    lastele = array[len(array) - 1]
    pixot = sorted([firstele, middleele, lastele])[1]
    if pixot == firstele:
        return array
    elif pixot == lastele:
        array[0], array[len(array) - 1] = array[len(array) - 1], array[0]
    else:
        array[0], array[(len(array) - 1) // 2] = array[(len(array) - 1) // 2], array[0]

    return array

if __name__ == "__main__":
    with open("QuickSort.txt") as infile:
        array = [int(lines.strip()) for lines in infile.readlines()]

#    array = [7, 5, 1, 4, 8, 3, 10, 2, 6, 9]
 #   array = [8, 10, 1, 9, 7, 2, 6, 3, 5, 4]
#    print(qsort(array, 1)[1])
 #   print(qsort(array, 2)[1])
    print(qsort(array, 3)[1])
