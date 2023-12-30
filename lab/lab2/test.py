from Matrix import Matrix
import numpy as np
import csv
import timeit
from ImprovedMatrix import improvedMatrix
for i in range(0,15):
    n=pow(2,i)
    a=np.random.randint(0, 30, size=(n, n))
    b=np.random.randint(0, 30, size=(n, n))
    execution_time_naive = timeit.timeit(lambda:Matrix.NaiveMultiply(a,b), number=1)
    print(execution_time_naive)
    execution_time_strassen = timeit.timeit(lambda: improvedMatrix.strassen_matrix_multiply(improvedMatrix,a,b), number=1)
   
    data=[n,execution_time_naive,execution_time_strassen]
    with open("data-3.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    

