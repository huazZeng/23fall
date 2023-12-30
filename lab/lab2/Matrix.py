import numpy as np

class Matrix:
    def Matrix_Add(a,b):
        n=len(a)
        
        result = np.zeros((n,n))
        for i in range(0,n):
            for j in range(0,n):
                result[i][j]=a[i][j]+b[i][j]
        return result

    def Matrix_Minus(a,b):
        n=len(a)
        
        result = np.zeros((n,n))
        for i in range(0,n):
            for j in range(0,n):
                result[i][j]=a[i][j]-b[i][j]
        return result

    def NaiveMultiply(a,b):
        if len(a[0])!=len(b):
            print("Math error")
        else:
            result = np.zeros((len(a),len(a)))
            for i in range(0,len(a)):
                for j in range(0,len(b[0])):
                    sum=0
                    for k in range(0,len(a[0])):
                        sum+=a[i][k]*b[k][j]
                    result[i][j]=sum
            return result


    #仅适用于n=2的k次方的方阵
    def StrassenMultiply(self,Matrix1,Matrix2):
        if len(Matrix1[0])!=len(Matrix2):
            print("Math error")
        
        else:
            N=len(Matrix1)
            
            if(N>1):
                result = np.zeros((N,N))
                n=(int)(N/2)
                a=Matrix1[:n,:n]
                b=Matrix1[:n,n:]
                c=Matrix1[n:,:n]
                d=Matrix1[n:,n:]
                e=Matrix2[:n,:n]
                f=Matrix2[:n,n:]
                g=Matrix2[n:,:n]
                h=Matrix2[n:,n:]
                P1=self.StrassenMultiply(self,a,self.Matrix_Minus(f,h))
                P2=self.StrassenMultiply(self,self.Matrix_Add(a,b),h)
                P3=self.StrassenMultiply(self,self.Matrix_Add(c,d),e)
                P4=self.StrassenMultiply(self,d,self.Matrix_Minus(g,e))
                P5=self.StrassenMultiply(self,self.Matrix_Add(a,d),self.Matrix_Add(e,h))
                P6=self.StrassenMultiply(self,self.Matrix_Minus(b,d),self.Matrix_Add(g,h))
                P7=self.StrassenMultiply(self,self.Matrix_Minus(a,c),self.Matrix_Add(e,f))

                R=self.Matrix_Minus(self.Matrix_Add(self.Matrix_Add(P4,P5),P6),P2)
                S=self.Matrix_Add(P1,P2)
                T=self.Matrix_Add(P3,P4)
                U=self.Matrix_Minus(self.Matrix_Minus(self.Matrix_Add(P1,P5),P3),P7)

                result1 = np.concatenate((R, S), axis=1)
                result2= np.concatenate((T, U), axis=1)
                result =np.concatenate((result1,result2),axis=0)
                return result
            else:
                return np.array([[Matrix1[0][0]*Matrix2[0][0]]])

    #copy from Chatgpt-3.5    
    def strassen_matrix_multiply(self,A, B):
        if len(A) == 1:
            return A * B
        
        # 分割输入矩阵为四个子矩阵
        n = len(A)
        n_half = n // 2
        A11 = A[:n_half, :n_half]
        A12 = A[:n_half, n_half:]
        A21 = A[n_half:, :n_half]
        A22 = A[n_half:, n_half:]
        
        B11 = B[:n_half, :n_half]
        B12 = B[:n_half, n_half:]
        B21 = B[n_half:, :n_half]
        B22 = B[n_half:, n_half:]
        
        # 递归计算七个部分
        P1 =self.strassen_matrix_multiply(self,A11 + A22, B11 + B22)
        P2 =self.strassen_matrix_multiply(self,A21 + A22, B11)
        P3 = self.strassen_matrix_multiply(self,A11, B12 - B22)
        P4 = self.strassen_matrix_multiply(self,A22, B21 - B11)
        P5 = self.strassen_matrix_multiply(self,A11 + A12, B22)
        P6 = self.strassen_matrix_multiply(self,A21 - A11, B11 + B12)
        P7 = self.strassen_matrix_multiply(self,A12 - A22, B21 + B22)
        
        # 计算结果的四个子矩阵
        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 - P2 + P3 + P6
        
        # 将四个子矩阵合并成结果矩阵
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
        
        return C

