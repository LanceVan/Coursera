from bigheap import BigHeap
from littleheap import LittleHeap


def openFile(filename):
    with open(filename) as infile:
        array = []
        for line in infile.readlines():
            array.append(int(line))
    return array

def medianmaintenance(array):
    littleheap = BigHeap()
    bigheap = LittleHeap()
    ans = []
    median = array.pop(0)
    ans.append(median)
    if array[0] < median:
        bigheap.insert(median)
        median = array[0]
    else:
        bigheap.insert(array[0])
    ans.append(median)
    array.pop(0)
    for item in array:
        if item > median:
            bigheap.insert(item)
        else:
            littleheap.insert(item)
        if bigheap.size() != littleheap.size():
            if bigheap.size() - littleheap.size() > 1:
                littleheap.insert(median)
                median = bigheap.extract()
            if littleheap.size() > bigheap.size():
                bigheap.insert(median)
                median = littleheap.extract()
        ans.append(median)
    return ans

if __name__ == "__main__":
    array = openFile("Median.txt")
    ans = medianmaintenance(array)
    print(ans)
    print(sum(ans))
