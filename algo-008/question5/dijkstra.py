class AdjList:

    def __init__(self):
        self.edge = []
        self.distance = []
        self.path = []
        self.size = 0

    def __len__(self):
        return self.size - 1

    def add(self, edges):
        for edge in edges:
            start = edge[0]
            terminal = edge[1]
            value = edge[2]
            while (self.size <= start) or (self.size <= terminal):
                self.edge.append([])
                self.distance.append(1000000)
                self.path.append(-1)
                self.size += 1

            self.edge[start].append({"start": start, "terminal": terminal, "value": value})
        return 0

    def check(self, start, terminal):
        return terminal in self.edge[start]

    def dijkstra(self, start):
        self.distance[start] = 0
        queue = [x for x in self.edge[start]]
        print(self.edge)
        for i in range(len(self) - 1):
            print(queue)
            mindis = 2147483647
            minedge = {}
            for edge in queue:
                tmpdis = self.distance[edge['start']] + edge['value']
                if tmpdis < mindis:
                    mindis = tmpdis
                    minedge = edge
            print(minedge)
            terminal = minedge['terminal']
            self.distance[terminal] = mindis
            for edge in self.edge[terminal]:
                queue.append(edge)
            i = 0
            queuetmp = []
            for edge in queue:
                if self.distance[edge['terminal']] >= 1000000:
                    queuetmp.append(edge)
            queue = queuetmp

def openFile(filename):
    with open(filename) as infile:
        edge = []
        for line in infile.readlines():
            tmplist = line.split('\t')
            start = int(tmplist[0])
            tmplist.pop()
            tmplist.pop(0)
            for tmpedge in tmplist:
                tmpedge = tmpedge.split(',')
                terminal = int(tmpedge[0])
                value = int(tmpedge[1])
                edge.append([start, terminal, value])

    return edge

if __name__ == "__main__":
    edges = openFile("dijkstraData.txt")
    print(edges)
    g = AdjList()
    g.add(edges)
    g.dijkstra(1)
    print(g.distance)
    problems = [7,37,59,82,99,115,133,165,188,197]
    for problem in problems:
        print(g.distance[problem])
