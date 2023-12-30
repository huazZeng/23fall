from InsertSort import InsertSort
class ConbindedtSort:
    def sort(self,arr,k):
        #在切割到k时 停止切割
        if len(arr)>k:
            mid=len(arr) // 2
            leftArr=arr[:mid]
            rightArr=arr[mid:]
            leftArr=self.sort(self,leftArr,k)
            rightArr=self.sort(self,rightArr,k)
        #合并
            i=0
            j=0
            k=0
            while i<len(rightArr) and j<len(leftArr):
                if rightArr[i] < leftArr [j]:
                    arr[k]=rightArr[i]
                    i+=1
                else:
                    arr[k]=leftArr[j]
                    j+=1
                k+=1
        #检查剩余元素
            while i<len(rightArr):
                arr[k]=rightArr[i]
                i+=1
                k+=1
            while j<len(leftArr):
                arr[k]=leftArr[j]
                j+=1
                k+=1
        #对切割的对象进行插入排序
        else:
            arr=InsertSort.sort(InsertSort,arr)
            
        return arr