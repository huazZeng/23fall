from collections import defaultdict, deque
class vertex:
    def __init__(self,value):
        self.value=value
        self.color=0
        self.d=-float("inf")
        self.pre=None
        self.begintime=None
        self.endtime=None

class Graph:
    def __init__(self):
        self.vertexs=[]
        #以邻接表形式表示
        self.edges=defaultdict(list)
        self.time=0
    def add_vertex(self,_vertex):
        self.vertexs.append(_vertex)

    def add_edge(self,src,dst,weigh):
        self.edges[src].append((dst,weigh))

    def DFS(self):
        self.time=0
        for v in self.vertexs:
            v.color=0
            v.pre=None
            v.begintime=None
            v.endtime=None
        for v in self.vertexs:
            if v.color==0:
                self.DFS_Visit(v)

    def DFS_Visit(self,source):
        self.time+=1
        source.begintime=self.time
        source.color=1
        for v in self.edges[source]:
            if v[0].color==0:
                self.DFS_Visit(v[0])
        source.color=2
        self.time += 1
        source.endtime=self.time

    
    def topological_sort(self):
        self.DFS()
        sorted_vertices = sorted(self.vertexs, key=lambda v: v.endtime, reverse=True)
        return sorted_vertices



    def PERT(self,topoq):
        lastone=None
        result=[]
        maxlength=0
        topoq[0].d=0
        topoq[0].pre=None
        for i in range(1,len(topoq)):
            for v in topoq :
                for e in self.edges[v]:
                    if e[0].d<v.d + e[1]:
                        e[0].d=v.d + e[1]
                        e[0].pre=v
                        if e[0].d > maxlength:
                            lastone=e[0]
                            maxlength=e[0].d
        for v in topoq :
            for e in self.edges[v]:
                if e[0].d<v.d+e[1]:
                    return False
        print('maxlength='+str(maxlength))
        x=lastone
        while x != None:
            result.append(x.value)
            x=x.pre
        for i in range(1,len(result)+1):
            print(str(result[-i])+'>  ',end='')
        print('')
        return True


values=[1,2,3,4,5,6,7,8,9,10]
graph = Graph()
for value in values:
    _vertex = vertex(value)
    graph.add_vertex(_vertex)
edges=([1,2,4],[1,4,4],[1,3,5],[2,5,4],[2,7,6],[3,5,5],[3,6,6],[4,6,7],
        [5,7,3],[5,8,4],[6,8,2],[6,9,2],[7,10,3],[8,10,2],[9,10,5])
for e in  edges:
    print(e)
    graph.add_edge(graph.vertexs[e[0]-1], graph.vertexs[e[1]-1],e[2])
quene=graph.topological_sort()
graph.PERT(quene)

values=[1,2,3,4,5,6]
graph = Graph()
for value in values:
    _vertex = vertex(value)
    graph.add_vertex(_vertex)
edges=([1,2,3],[1,3,2],[2,5,3],[2,4,2],[3,4,4],[3,6,3],[4,6,2],[5,6,1],)
for e in  edges:
    graph.add_edge(graph.vertexs[e[0]-1], graph.vertexs[e[1]-1],e[2])
quene=graph.topological_sort()
graph.PERT(quene)

values=[1,2,3,4,5,6]
graph = Graph()
for value in values:
    _vertex = vertex(value)
    graph.add_vertex(_vertex)
edges=([1,2,3],[1,3,8],[2,5,6],[2,4,9],[3,2,4],[3,5,10],[4,6,6],[5,6,9],)
for e in  edges:
    graph.add_edge(graph.vertexs[e[0]-1], graph.vertexs[e[1]-1],e[2])
quene=graph.topological_sort()
graph.PERT(quene)

values=[1,2,3,4,5,6,7,8,9]
graph = Graph()
for value in values:
    _vertex = vertex(value)
    graph.add_vertex(_vertex)
edges=([1,2,2],[1,3,5],[1,5,5],[2,4,3],[2,3,2],[3,6,3],[3,5,1],[4,6,2],[5,7,6],
        [6,8,4],[6,7,3],[7,9,4],[8,9,2])
for e in  edges:
    graph.add_edge(graph.vertexs[e[0]-1], graph.vertexs[e[1]-1],e[2])
quene=graph.topological_sort()
graph.PERT(quene)