class schedule_model_Greedy:
    def __init__(self,duties):
        self.duties=duties
    
    def sort(self):
        self.duties = sorted(self.duties, key=lambda x: (-x[1],x[2],-(x[1]/x[0])))
        
    def schedule(self):
        totalProfit = 0
        currentTime = 0
        scheduledduties = [False] * len(self.duties)
        for i in range(len(self.duties)):
            if currentTime + self.duties[i][0] <= self.duties[i][2]:
                scheduledduties[i] = True
                currentTime += self.duties[i][0]
                totalProfit += self.duties[i][1]
        print(totalProfit)
#采用类似0-1背包的动态规划算法
class schedule_model_Dynamic:
    def __init__(self,duties):
        self.duties=duties
    
    def sort(self):
        for i in range(len(self.duties) - 1, -1, -1):
            if self.duties[i][0] > self.duties[i][2]:
                del self.duties[i]
        self.duties = sorted(self.duties, key=lambda x: x[2])
        
        
    def schedule(self):
        currunttime=0
        m=len(self.duties)
        n=self.duties[m-1][2]
        p = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j  in range(1,n+1):
                #当前时间不能执行任务时
                if(j<self.duties[i-1][0]):
                    p[i][j]=p[i-1][j]
                #当前时间已经超过DDL
                elif(j>self.duties[i-1][2]):
                    for k in range(j):
                        if not p[i][j-k] == 0:
                            p[i][j]=p[i][j-k]
                            break
                ##判断做这个job和不做这个job 哪个收益高
                else:
                    p[i][j]=max(p[i-1][j],p[i-1][j-self.duties[i-1][0]]+self.duties[i-1][1])
        print(p[m][n])
        
        
if __name__ =="__main__":
        sample_jobs = [
        [(2, 60, 3), (1, 100, 2), (3, 20, 4), (2, 40, 4)],
        [(3, 100, 4), (1, 80, 1), (2, 70, 2), (1, 10, 3)],
        [(4, 100, 4), (2, 75, 3), (3, 50, 3), (1, 25, 1)],
        [(2, 60, 3), (1, 100, 2), (3, 20, 3), (2, 40, 2), (2, 50, 3)],
        [(2, 60, 3), (1, 100, 2), (3, 20, 4), (2, 40, 4), (2, 50, 3), (1, 80, 2)],
        [(2, 60, 3), (1, 100, 2), (3, 20, 3), (2, 40, 2), (2, 50, 3), (1, 80, 2), (4, 90, 4)],
        [(3, 60, 3), (2, 100, 2), (1, 20, 2), (2, 40, 4), (4, 50, 4)],
        [(2, 60, 3), (1, 100, 2), (3, 20, 3), (2, 40, 2), (4, 50, 4), (1, 80, 2), (4, 90, 4)],
        [(3, 60, 3), (2, 100, 2), (1, 20, 2), (2, 40, 2), (4, 50, 4), (5, 70, 5)],
        [(2, 60, 3), (1, 100, 2), (3, 20, 3), (2, 40, 2), (4, 50, 4), (5, 70, 5), (3, 90, 4)]
    ]
        
        for i in range(len(sample_jobs)):
            data=sample_jobs[i]
            model=schedule_model_Dynamic(data)
            model.sort()
            model.schedule()
        print('---------------------------------')

        for i in range(len(sample_jobs)):
            data=sample_jobs[i]
            model_2=schedule_model_Greedy(data)
            model_2.sort()
            model_2.schedule()