import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.shortestpath = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.edges[vertex] = {}
            self.shortestpath[vertex]={}

    def add_edge(self, src, dst, weight=1):
        self.edges[src][dst] = weight

    def dijkstra(self, start):
        # 初始化最短路径字典
        shortest_paths = {vertex: {'distance': float('inf'), 'path': []} for vertex in self.vertices}
        shortest_paths[start]['distance'] = 0

        # 优先队列，用于按距离维护顶点
        min_heap = [(0, start)]

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            for neighbor, weight in self.edges[current_vertex].items():
                distance = current_distance + weight
                if distance < shortest_paths[neighbor]['distance']:
                    shortest_paths[neighbor]['distance'] = distance
                    shortest_paths[neighbor]['path'] = shortest_paths[current_vertex]['path'] + [current_vertex]
                    heapq.heappush(min_heap, (distance, neighbor))
        self.shortestpath[start]=shortest_paths
        return shortest_paths
    def kruskal(self):
        mst = []
        edges = []
        totallength=0.0
        for src in self.vertices:
            for dst, weight in self.edges[src].items():
                edges.append((weight, src, dst))
        edges.sort()
        parent = {vertex: vertex for vertex in self.vertices}
        def find_set(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find_set(parent[vertex])
            return parent[vertex]
        def union(u, v):
            root_u = find_set(u)
            root_v = find_set(v)
            parent[root_u] = root_v
        for weight, src, dst in edges:
            if find_set(src) != find_set(dst):
                mst.append((src, dst, weight))
                totallength+=weight
                union(src, dst)

        return mst,totallength

    def prim(self, start):
            mst = []
            min_heap = [(0, start, None)]
            visited = set()
            while min_heap:
                current_distance, current_vertex, parent = heapq.heappop(min_heap)
                if current_vertex in visited:
                    continue
                if parent is not None:
                    mst.append((parent, current_vertex, current_distance))
                visited.add(current_vertex)
                for neighbor, weight in self.edges[current_vertex].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (weight, neighbor, current_vertex))

            return mst
    def subwaypath(self,start):
            pathincludingedges=[]
            totallength=0.0
            for v in self.vertices:
                current_vertex=start
                Path=self.shortestpath[start][v]['path']+[v]
                for vedge in Path:
                    
                    if vedge==start:
                        continue
                    edge=(current_vertex,vedge)
                    
                    if edge not in pathincludingedges:
                        
                        pathincludingedges.append(edge)
                        print(edge)
                        totallength+=self.edges[current_vertex][vedge]
        
                    current_vertex=vedge
            return pathincludingedges,totallength

    def bellman_ford(self, start):
        # 初始化最短路径字典
        shortest_paths = {vertex: {'distance': float('inf'), 'path': []} for vertex in self.vertices}
        shortest_paths[start]['distance'] = 0

        # 松弛操作
        for _ in range(len(self.vertices) - 1):
            for src in self.vertices:
                for dst, weight in self.edges[src].items():
                    distance = shortest_paths[src]['distance'] + weight
                    if distance < shortest_paths[dst]['distance']:
                        shortest_paths[dst]['distance'] = distance
                        shortest_paths[dst]['path'] = shortest_paths[src]['path'] + [src]

        self.shortestpath[start] = shortest_paths
        return shortest_paths

    def floyd_warshall(self):
        # 初始化最短路径字典
        shortest_paths = {src: {dst: {'distance': float('inf'), 'path': []} for dst in self.vertices} for src in self.vertices}

        # 设置直接相邻的节点的距离和路径
        for src in self.vertices:
            for dst, weight in self.edges[src].items():
                shortest_paths[src][dst]['distance'] = weight
                shortest_paths[src][dst]['path'] = [src]

        # Floyd-Warshall算法主循环
        for mid in self.vertices:
            for src in self.vertices:
                for dst in self.vertices:
                    if shortest_paths[src][mid]['distance'] + shortest_paths[mid][dst]['distance'] < shortest_paths[src][dst]['distance']:
                        shortest_paths[src][dst]['distance'] = shortest_paths[src][mid]['distance'] + shortest_paths[mid][dst]['distance']
                        shortest_paths[src][dst]['path'] = shortest_paths[src][mid]['path'] + shortest_paths[mid][dst]['path'][1:]

        return shortest_paths                
                    
                
# graph=Graph()
# filepath='data-1\edge.txt'
# i=0
# with open(filepath,'r') as file:
#             for line in file:
#                 i+=1
#                 line = line.strip()
#                 parts = line.split()
#                 if len(parts) == 3:
#                     source_node, target_node, weight = parts
#                     graph.add_vertex(source_node)
#                     graph.add_vertex(target_node)
#                     graph.add_edge(source_node,target_node,float(weight))
#                     graph.add_edge(target_node,source_node,float(weight))
# print(i)

# for v in graph.vertices:          
#     graph.shortestpath[v]=graph.dijkstra(v)

# print(graph.subwaypath('A'))
        

    