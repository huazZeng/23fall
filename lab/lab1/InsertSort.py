class InsertSort:
    def sort(self,source):
        for i in range(1,len(source)):
            key=source[i]
            preIndex=i-1
            while preIndex>=0 and  key<source[preIndex]:
                source[preIndex+1]=source[preIndex]
                preIndex-=1
            source[preIndex+1]=key
            
        return source

            