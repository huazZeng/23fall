from BR_Tree import BR_Tree
from B_Tree import BTree
import time 
import csv
import timeit

def insertall(br,data_insert):
        for i in range(1,len(data_insert)):
                br.insert(data_insert[i])
                
        
           
   
def deleteall(br,data_delete):
     for i in range(1,len(data_delete)):
        br.delete(data_delete[i])


with open('dataset\initial.txt','r',encoding='utf-8') as file:
        data = [line.strip().split() for line in file]
with open('.\dataset\delete.txt','r',encoding='utf-8') as file:
        data_delete = [line.strip() for line in file]
with open('.\dataset\insert.txt','r',encoding='utf-8') as file:
        data_insert = [line.strip().split() for line in file]

with open(".\data-BR.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    initialize_endtime=0.0
    delete_endtime=0.0
    insert_endtime=0.0

    for i in range(10):
        br=BTree(5)
        
        initialize_endtime+=timeit.timeit(lambda:insertall(br,data), number=1)
   
        delete_endtime+=timeit.timeit(lambda:deleteall(br,data_delete), number=1)
        insert_endtime+=timeit.timeit(lambda:insertall(br,data_insert), number=1)
    
        datas=[initialize_endtime/10,delete_endtime/10,insert_endtime/10]
    writer.writerow(datas)


    
    ##test B
    






