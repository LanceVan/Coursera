import copy
import random

def openFile(filename):
    with open(filename) as infile:
        adjList = [[0], ]
        for line in infile.readlines():
            tmpList = []
            elements = line.split('\t')
            elements.pop()
            tmpList = [int(element) for element in elements]
            tmpList.pop(0)
            print(tmpList)
            adjList.append(tmpList)

    return adjList

def root(set, element):
    if element != set[element]:
        return root(set, set[element])
    else:
        return element

def randomContract(adjList):
    set = [x for x in range(len(adjList))]
    for x in range(len(adjList) - 3):
        randomvertice = random.randint(1, len(adjList) - 1)
        while len(adjList[randomvertice]) == 0:
            randomvertice = random.randint(1, len(adjList) - 1)
        delvertice = adjList[randomvertice][random.randint(1, len(adjList[randomvertice])) - 1]
        set[root(set, delvertice)] = set[root(set, randomvertice)]
        for element in set:
            element = root(set, element)
        vertice = 0
        for origin in adjList[1:]:
            vertice += 1
            if len(origin) > 0:
                terminalnum = 0
                while terminalnum < len(origin):
                    if set[vertice] == set[origin[terminalnum]]:
                        origin.pop(terminalnum)
                    else:
                        terminalnum += 1
#        print(randomvertice, delvertice)
 #       print(set)
  #      print(adjList)

    ans = sum([len(vertice) for vertice in adjList])
    return (ans - 1) / 2

if __name__ == "__main__":
    adjList = openFile(filename="kargerMinCut.txt")
    tmpList = copy.deepcopy(adjList)
    minans = sum([len(vertice) for vertice in adjList])
    while True:
        ans = randomContract(adjList)
        if ans < minans:
            minans = ans
        print(minans)
        adjList = copy.deepcopy(tmpList)
