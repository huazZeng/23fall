#  Lab 8
##实验思路
基于Lab 7图算法的基本操作的实现，添加用于查找最大路径的**Bellman-Ford**算法,该算法时间复杂度为**O(V*E)**

##代码
```python
    def PERT(self,topoq):
        lastone=None
        maxlength=0
        topoq[0].d=0
        topoq[0].pre=None
        #更新n-1次
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
        print(maxlength)
        x=lastone
        #根据记录的信息 反推路径
        while x != None:
            print(x.value)
            x=x.pre
        
        return True
```

##Result
maxlength=18
1>  3>  6>  9>  10
maxlength=8
1>  3>  4>  6
maxlength=27
1>  3>  2>  4>  6
maxlength=16
1>  3>  5>  7>  9