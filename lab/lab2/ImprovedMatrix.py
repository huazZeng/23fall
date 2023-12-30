import numpy as np
from Matrix import Matrix 
class improvedMatrix():
    def strassen_matrix_multiply(self,A, B):
        if len(A) <= 32:
            return Matrix.NaiveMultiply(A,B)
        
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