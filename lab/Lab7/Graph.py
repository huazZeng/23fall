from collections import defaultdict, deque
class vertex:
    def __init__(self,value):
        self.value=value
        self.color=0
        self.d=float("inf")
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
    def add_edge(self,src,dst):
        self.edges[src].append(dst)

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
            if v.color==0:
                self.DFS_Visit(v)
        source.color=2
        self.time += 1
        source.endtime=self.time

    
    def topological_sort(self):
        self.DFS()
        sorted_vertices = sorted(self.vertexs, key=lambda v: v.endtime, reverse=True)
        return sorted_vertices



    def DFS_s(self, source, dst):
        stack = [(source, [source.value])]
        paths = []

        while stack:
            current_vertex, path = stack.pop()  # pop from the end of the list (top of the stack)

            for neighbor in self.edges[current_vertex]:
                if neighbor.value not in path:
                    if neighbor == dst:
                        paths.append(path + [neighbor.value])
                    else:
                        stack.append((neighbor, path + [neighbor.value]))

        return paths

##课程排序
values = [0,1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15]
graph = Graph()
for value in values:
    _vertex = vertex(value)
    graph.add_vertex(_vertex)
graph.add_edge(graph.vertexs[1], graph.vertexs[3])
graph.add_edge(graph.vertexs[1], graph.vertexs[2])
graph.add_edge(graph.vertexs[1], graph.vertexs[4])
graph.add_edge(graph.vertexs[3], graph.vertexs[2])
graph.add_edge(graph.vertexs[3], graph.vertexs[6])
graph.add_edge(graph.vertexs[4], graph.vertexs[6])
graph.add_edge(graph.vertexs[4], graph.vertexs[10])
graph.add_edge(graph.vertexs[5], graph.vertexs[2])
graph.add_edge(graph.vertexs[5], graph.vertexs[6])
graph.add_edge(graph.vertexs[6], graph.vertexs[10])
graph.add_edge(graph.vertexs[6], graph.vertexs[7])
graph.add_edge(graph.vertexs[8], graph.vertexs[6])
graph.add_edge(graph.vertexs[8], graph.vertexs[9])
graph.add_edge(graph.vertexs[8], graph.vertexs[11])
graph.add_edge(graph.vertexs[9], graph.vertexs[6])
graph.add_edge(graph.vertexs[12], graph.vertexs[13])
graph.add_edge(graph.vertexs[12], graph.vertexs[11])
graph.add_edge(graph.vertexs[13], graph.vertexs[10])
graph.add_edge(graph.vertexs[13], graph.vertexs[4])
graph.add_edge(graph.vertexs[14], graph.vertexs[10])
for i in range(1,15):
    graph.add_edge(graph.vertexs[i], graph.vertexs[15])
    graph.add_edge(graph.vertexs[i], graph.vertexs[0])
graph.add_edge(graph.vertexs[15], graph.vertexs[0])
int2course={1:'Java or C++',2:'Web Application',3:'OOP',4:'Data STtructure and Algorithm',
            5:'Database',6:'Software Engineering',7:'Project Management',8:'Compter System',
            9:'Computer Network',10:'Intelligent systems',11:'computer Architecture',12:'Calculus',
            13:'Probabllity and Statistics',14:'Discrete Mathematics',15:'Intership',0:'Thesis'}
print("拓扑排序结果:")
topological_order = graph.topological_sort()
for vertex1 in topological_order:
    print(f"Vertex: {int2course[vertex1.value]}, Timestamp: {vertex1.endtime}")

###过河问题
values = [[0,0,0,0],[0,0,0,1], [0,0,1,0],[0,0,1,1], [0,1,0,0], [0,1,0,1], [0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
graph2 = Graph()
for value in values:
    _vertex = vertex(value)
    graph2.add_vertex(_vertex)
for i in values:
    for j in values:
        if j==[0,0,1,1] or j==[0,1,1,1]  or j==[0,1,1,0] or j==[1,0,0,0] or j==[1,1,0,0] or j==[1,0,0,1]:
            continue
    
        if(i[0]==0 and j[0]==1):
            count = 0
            for k in range(1,4):
                if(i[k]==1 and j[k]==0):
                    count = 5
                    break
                if(i[k]==0 and j[k]==1):
                    count+=1
            if count <2 :
                graph2.add_edge(graph2.vertexs[i[0]*8+i[1]*4+i[2]*2+i[3]], graph2.vertexs[j[0]*8+j[1]*4+j[2]*2+j[3]])
                
        if(i[0]==1 and j[0]==0):
            count = 0
            for k in range(1,4):
                if(i[k]==0 and j[k]==1):
                    count = 5
                    break
                if(i[k]==1 and j[k]==0):
                    count+=1
            if count<2 :
                graph2.add_edge(graph2.vertexs[i[0]*8+i[1]*4+i[2]*2+i[3]], graph2.vertexs[j[0]*8+j[1]*4+j[2]*2+j[3]])
                
             
print(graph2.DFS_s(graph2.vertexs[0],graph2.vertexs[15]))