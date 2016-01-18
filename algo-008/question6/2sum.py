def openFile(filename):
    with open(filename) as infile:
        array = []
        for line in infile.readlines():
            array.append(int(line))
        array = list(set(array))
        return array

def binsearch(array, num):
    i = 0
    j = len(array) - 1
    while i != j:
        mid = (i + j) // 2
        if num > array[mid]:
            i = mid
        else:
            j = mid
    return i

def twosum(array):
    array.sort()
    i = 0
    j = len(array) - 1
    ans = set()
    while i < j:
        print(i, j)
        if array[i] + array[j] > 10000:
            j -= 1
            continue
        if array[i] + array[j] > -10000:
            k = j
            while -10000 <= array[i] + array[k] <= 10000:
                ans.add(array[i] + array[k])
                k -= 1
        i += 1

    return len(ans)

if __name__ == "__main__":
    array = openFile('2sum.txt')
    print(twosum(array))
