from graph import Graph

class model:
    def __init__(self):
        self.graph=Graph()
        self.getmap()
    
    def getmap(self):
        filepath='data-1\edge.txt'
        with open(filepath,'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split()
                if len(parts) == 3:
                    source_node, target_node, weight = parts
                    self.graph.add_vertex(source_node)
                    self.graph.add_vertex(target_node)
                    self.graph.add_edge(source_node,target_node,float(weight))
                    self.graph.add_edge(target_node,source_node,float(weight))
        for v in self.graph.vertices:          
            shortest=self.graph.dijkstra(v)
    
    


    def GetShortestPathFromTo(self,a,b):
        return self.graph.shortestpath[a][b]
    
    def GetAllShortestPathFrom(self,a):
        return self.graph.shortestpath[a]

    def GetShortestPathPassAll(self):
        return self.graph.kruskal()

        
    def GetShortestPathBeginOn(self,A):
        return self.graph.subwaypath(A)
