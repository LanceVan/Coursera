def mergeAndCountSplitInv(array):
    mid = len(array) // 2
    invs = 0
    ans = []
    i = 0
    j = mid
    while i < mid and j < len(array) and i < j:
        if array[i] > array[j]:
            invs += mid - i
            ans.append(array[j])
            j += 1
        else:
            ans.append(array[i])
            i += 1

    if i < mid:
        ans = ans + array[i : mid]
    if j < len(array):
        ans = ans + array[j :]

    return ans, invs

def sortAndCount(array):
    if len(array) <= 1:
        return array, 0
    else:
        array[: len(array) // 2], x = sortAndCount(array[: len(array) // 2])
        array[len(array) // 2 :], y = sortAndCount(array[len(array) // 2 :])
        array, z = mergeAndCountSplitInv(array)
        return array, x + y + z

if __name__ == "__main__":
    with open("IntegerArray.txt") as infile:
        array = [int(lines.strip()) for lines in infile.readlines()]

    print(sortAndCount(array))
    
