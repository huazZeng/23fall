class MergeSort:
    def sort(self,arr):
        #拆分递归
        if len(arr)>1:
            mid=len(arr) // 2
            leftArr=arr[:mid]
            rightArr=arr[mid:]
            leftArr=self.sort(leftArr)
            rightArr=self.sort(rightArr)
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
        return arr
        
        
        