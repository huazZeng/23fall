#Lab7
##思路
###课程排序
先根据课程依赖关系生成有向图
而后DFS遍历 给每个课程打上时间戳
最后根据时间戳输出结果

###过河问题
同样先根据现实条件生成有向图
```python
##以下为生成图的代码
for i in values:
    for j in values:
        ##排除特殊情况
        if j==[0,0,1,1] or j==[0,1,1,1]  or j==[0,1,1,0] or j==[1,0,0,0] or j==[1,1,0,0] or j==[1,0,0,1]:
            continue
        ##从左到右时 其他三个物品至多一个被移动 以此判断 是否能够有转化关系 
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
        ##从右到左时 其他三个物品至多一个被移动 以此判断 是否能够有转化关系        
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
```
而后进行基于栈结构的DFS 得到所有路径


##result
**拓扑排序结果**
Vertex: Discrete Mathematics, Timestamp: 32
Vertex: Calculus, Timestamp: 30
Vertex: Probabllity and Statistics, Timestamp: 29
Vertex: Compter System, Timestamp: 26
Vertex: computer Architecture, Timestamp: 25
Vertex: Computer Network, Timestamp: 23
Vertex: Database, Timestamp: 20
Vertex: Java or C++, Timestamp: 18
Vertex: Data STtructure and Algorithm, Timestamp: 17
Vertex: OOP, Timestamp: 15
Vertex: Software Engineering, Timestamp: 14
Vertex: Project Management, Timestamp: 13
Vertex: Intelligent systems, Timestamp: 11
Vertex: Web Application, Timestamp: 8
Vertex: Intership, Timestamp: 7
Vertex: Thesis, Timestamp: 2
**过河问题结果**
PS：从前到后分别为 Farmer Wolf Goat Cabbage 0表示左侧 1表示右侧
[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 1], [0, 0, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1],

[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1]