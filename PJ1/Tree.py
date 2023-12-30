class Tree:
    def __init__(self):
        raise NotImplementedError("Subclasses must implement initialize method")
    
    def initialize(self):
        raise NotImplementedError("Subclasses must implement initialize method")

    def insert(self, key):
        raise NotImplementedError("Subclasses must implement insert method")

    def delete(self, key):
        raise NotImplementedError("Subclasses must implement delete method")

    def searchByEng(self, key):
        raise NotImplementedError("Subclasses must implement search method")

    def searchByRange(self,_from,to):
        raise NotImplementedError("Subclasses must implement initialize method")