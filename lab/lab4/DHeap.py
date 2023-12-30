class DHeap:
    def __init__(self,D,array):
        self.D=D
        self.HeapArray=array
        self.size=len(self.HeapArray)-1
        self.lastParent=int((self.size+D-2)/D)
        

    def ExtractMax(self):
        max=self.HeapArray[1]
        self.HeapArray[1]=self.HeapArray[self.size]
        self.size-=1
        self.Heapifyall()
        return max
    
    def IncreaseKey(self,index,key):
        D=self.D
        if self.HeapArray[index]>key:
            print("error")
        else:
            self.HeapArray[index]=key
            while(self.HeapArray[index]>self.HeapArray[int((index+D-2)/D)] and index>0):
                self.HeapArray[index],self.HeapArray[int((index+D-2)/D)]=self.HeapArray[int((index+D-2)/D)],self.HeapArray[index]
                index=int((index+D-2)/D)
            print("successful increasing")

    def Insert(self):
        index=len(self.D)
        self.HeapArray.append(0)
        self.size+=1
        self.IncreaseKey(self,index,self.size)

    def Heapify(self,index):
        largest = self.HeapArray[index]
        largestindex=index
        D=self.D
        for i in range(0,self.D):
            if index*D-D+2+i<=self.size and self.HeapArray[index*D-D+2+i] > largest :
                largestindex=index*D-D+2+i
                largest = self.HeapArray[index*D-D+2+i]
        if largestindex != index:
            self.HeapArray[index],self.HeapArray[largestindex]=self.HeapArray[largestindex],self.HeapArray[index]
            if(largestindex<=self.lastParent):
                self.Heapify(largestindex)

        
    def Heapifyall(self):
        for i in range (0,self.lastParent):
            self.Heapify(self.lastParent-i)
        

        
        
        
