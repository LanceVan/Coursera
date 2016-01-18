class AdjList:

    def __init__(self):
        self.edge = []
        self.pointf = []
        self.pointbelong = []
        self.flag = 0

    def add(self, edges):
        for edge in edges:
            start = edge[0]
            end = edge[1]
            while (len(self.edge) <= start) or (len(self.edge) <= end):
                self.edge.append([])
                self.pointf.append(0)
                self.pointbelong.append(0)
            self.edge[start].append(end)
        return 0

    def check(self, start, end):
        return end in self.edge[start]

def openFile(filename):
    with open(filename) as infile:
        edge = []
        edgerev = []
        for line in infile.readlines():
            tmplist = line.split(' ')
            tmplist[0] = int(tmplist[0])
            tmplist[1] = int(tmplist[1])
            edge.append([tmplist[0], tmplist[1]])
            edgerev.append([tmplist[1], tmplist[0]])

    return edge, edgerev

def dfs(adjlist, start):
    queue = [start]
    while queue != []:
        flag = 0
        for end in adjlist.edge[queue[-1]]:
            if adjlist.pointbelong[end] == 0:
                flag = 1
                adjlist.pointbelong[end] = adjlist.pointbelong[queue[-1]]
                queue.append(end)
                break
        if flag == 0:
            adjlist.pointf[queue[-1]] = max(adjlist.pointf) + 1
            queue.pop()

    return adjlist

if __name__ == "__main__":
    edges, edgesrev = openFile("SCC.txt")
    g = AdjList()
    g.add(edges)
    l = len(g.edge) - 1
    print(1)
    while l > 0:
        print(l)
        if g.pointbelong[l] == 0:
            g.pointbelong[l] = l
            g = dfs(g, l)
        l -= 1

    for edgerev in edgesrev:
        edgerev[0] = g.pointf[edgerev[0]]
        edgerev[1] = g.pointf[edgerev[1]]

    print(2)

    grev = AdjList()
    grev.add(edgesrev)

    l = len(grev.edge) - 1
    while l > 0:
        print(l)
        if grev.pointbelong[l] == 0:
            grev.pointbelong[l] = l
            grev = dfs(grev, l)
        l -= 1

    grev.pointbelong.sort(reverse = True)
    ans = []
    continuous = 0
    flag = grev.pointbelong[0]
    for element in grev.pointbelong:
        if element == flag:
            continuous += 1
        else:
            ans.append(continuous)
            flag = element
            continuous = 1
    ans.sort()
    print(ans)
