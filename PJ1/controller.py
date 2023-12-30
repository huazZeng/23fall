from  BR_Tree import BR_Tree
from B_Tree import BTree
class controller:
    def __init__(self):
        self.TreeType=0
        self.tree=BTree(5)
        self.path="dataset/bt.txt"
    def changetype(self,n):
        self.TreeType=n
        if self.TreeType==0:
            self.tree=BTree(5)
            self.path="dataset/bt.txt"
        else :
            self.tree=BR_Tree()
            self.path="dataset/brt.txt"
    def importfrom(self,_path):
        with open(_path,'r',encoding='utf-8') as file:
            self.data = [line.strip().split() for line in file]
        
        print(self.data[0])
        if self.data[0][0]=='INSERT':
            for i in range(1,len(self.data)):
                self.tree.insert(self.data[i])
        if self.data[0][0]=='DELETE':
            for i in range(1,len(self.data)):
                self.tree.delete(self.data[i][0])
                print(self.data[i][0])

        self.tree.result=''
        self.tree.preorder_traversal(self.tree.root,0)
        with open(self.path, 'w', encoding='utf-8') as file:
            writer = file.write
            writer(self.tree.result)
        return self.tree.result



    def search(self,key):
        result =self.tree.searchByEng(self.tree.root,key)
        if  result!= None :
            return result
        else:
            return "No such word"
    def delete(self,key):
        self.tree.delete(key)
        
    def add(self,key,value):
        k=[key,value]
        self.tree.insert(k)



    def searchByRange(self,_from,to):
        self.tree.result=''
        self.tree.searchByRange(self.tree.root,_from,to)
        return self.tree.result
        


    