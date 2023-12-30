from map_model import model
from connection_sql import onlinesearch
class controller:
    def __init__(self):
        self.model=model()
        self.isOnline=False
        self.onlinesearch=onlinesearch()
    def operation_1(self,A,B):
        if(not self.isOnline):
            resultdist=self.model.GetShortestPathFromTo(A,B)
            result=resultdist['path']+[B]
            string=str(resultdist['distance'])+'  '+str(result)
            return string
        else:
            return self.onlinesearch.operation_1(A,B)
    def operation_2(self,A):
        string=''
        if(not self.isOnline):
            resultdist=self.model.GetAllShortestPathFrom(A)
            for vertex, info in resultdist.items():
                string+=f"Shortest path from {A} to {vertex}: {info['distance']}, Path: {info['path'] + [vertex]}\n"
            return string
        else:
            return self.onlinesearch.operation_2(A)    
    def operation_3(self):
        string='Shortest path passing all location including edges:'
        if(not self.isOnline):
            resultlist,totallength=self.model.GetShortestPathPassAll()
            for a in resultlist:
                string+=f"({a[0],a[1]}),"
            string+=f"\ntotallength is {totallength} "
            return string
        else:
            return self.onlinesearch.operation_3()
    def operation_4(self,A):
        string='subway path including edges:'
        if(not self.isOnline):
            resultlist,totallength=self.model.GetShortestPathBeginOn(A)
            for a in resultlist:
                string+=f"({a[0],a[1]}),"
            string+=f"\ntotallength is {totallength} "
            return string
        else:
            return self.onlinesearch.operation_4(A)


