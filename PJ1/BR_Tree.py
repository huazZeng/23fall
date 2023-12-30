from NodeforBR import NodeforBR
from Tree import Tree
class BR_Tree(Tree):
    def __init__(self):
        self.nil = NodeforBR(0, None,None,None) 
        self.root = self.nil
        self.result=''
    def insert(self, keys):
        
        key=keys[0]
        value=keys[1]
        if self.search(key)==self.nil:
            new_node = NodeforBR(1, key,value,self.nil)
            new_node.leftchild = self.nil
            new_node.rightchild = self.nil
            if self.root == self.nil:
                self.root = new_node
                new_node.redbool = 0
                new_node.leftchild = self.nil
                new_node.rightchild = self.nil
            else:
                current = self.root
                while current != self.nil:
                    parent = current
                    if key < current.key:
                        current = current.leftchild
                    else:
                        current = current.rightchild
                new_node.parent = parent
                if key < parent.key:
                    parent.leftchild = new_node
                else:
                    parent.rightchild = new_node
                self.insert_fixup(new_node)
        else: return

    def insert_fixup(self, node):
            while node!=self.root and node.parent.redbool :
                if node.parent == node.parent.parent.leftchild:
                    uncle = node.parent.parent.rightchild
                    if uncle.redbool:
                        node.parent.redbool = 0
                        uncle.redbool = 0
                        node.parent.parent.redbool = 1
                        node = node.parent.parent
                    else:
                        if node == node.parent.rightchild:
                            node = node.parent
                            self._left_rotate(node)
                        node.parent.redbool = 0
                        node.parent.parent.redbool = 1
                        self._right_rotate(node.parent.parent)
                else:
                    uncle = node.parent.parent.leftchild
                    if uncle.redbool:
                        node.parent.redbool = 0
                        uncle.redbool = 0
                        node.parent.parent.redbool = 1
                        node = node.parent.parent
                    else:
                        if node == node.parent.leftchild:
                            node = node.parent
                            self._right_rotate(node)
                        node.parent.redbool = 0
                        node.parent.parent.redbool = 1
                        self._left_rotate(node.parent.parent)
            self.root.redbool = 0    
            
    def preorder_traversal(self,node,level):
        if node != self.nil :
            self.result+=str(node.key)+' '+str(node.value)+' '+str(node.redbool)+' level='+str(level) +' left child:' +str(node.leftchild.key)+' right child:' +str(node.rightchild.key)+'\n'  # 先访问当前节点的值
            self.preorder_traversal(node.leftchild,level+1)
            self.preorder_traversal(node.rightchild,level+1)  


    def searchByEng(self,node,key):
        return self.search(key).value

    def search(self,key):
        current =self.root
        while current!=self.nil  and  current.key != key :
            if current.key>key:
                current = current.leftchild
            else:
                current = current.rightchild
        return current


    def _left_rotate(self, x):
        y = x.rightchild
        x.rightchild = y.leftchild
        if y.leftchild != self.nil:
            y.leftchild.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.leftchild:
            x.parent.leftchild = y
        else:
            x.parent.rightchild = y
        y.leftchild = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.leftchild
        y.leftchild = x.rightchild
        if x.rightchild != self.nil:
            x.rightchild.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.leftchild:
            y.parent.leftchild = x
        else:
            y.parent.rightchild = x
        x.rightchild = y
        y.parent = x

    

   
            
    # def delete(self, node):
    #     z = node
    #     if z == self.nil:
    #         return
    #     y = z
    #     y_original_redbool = y.redbool
    #     if z.leftchild == self.nil:
    #         x = z.rightchild
    #         self._transplant(z, z.rightchild)
    #     elif z.rightchild == self.nil:
    #         x = z.leftchild
    #         self._transplant(z, z.leftchild)
    #     else:
    #         y = self._find_successor(z)
    #         y_original_redbool = y.redbool
    #         x = y.rightchild
    #         if y.parent == z:
    #             x.parent = y
    #         else:
    #             self._transplant(y, y.rightchild)
    #             y.rightchild = z.rightchild
    #             y.rightchild.parent = y
    #         self._transplant(z, y)
    #         y.leftchild = z.leftchild
    #         y.leftchild.parent = y
    #         y.redbool = z.redbool
    #     if y_original_redbool == 0:
    #         self._delete_fixup(x)

    # def _find_successor(self, node):
    #     current = node.rightchild
    #     while current.leftchild != self.nil:
    #         current = current.leftchild
    #     return current
    # def _delete_fixup(self, x):
    #     while x != self.root and x is not None and x.redbool == 0:
    #         if x == x.parent.leftchild:
    #             w = x.parent.rightchild
    #             if w.redbool == 1:
    #                 w.redbool = 0
    #                 x.parent.redbool = 1
    #                 self._left_rotate(x.parent)
    #                 w = x.parent.rightchild
    #             if w!=self.nil and w.leftchild.redbool == 0 and w.rightchild.redbool == 0:
    #                 w.redbool = 1
    #                 x = x.parent
    #             else:
    #                 if  w!=self.nil and w.rightchild.redbool == 0:
    #                     w.leftchild.redbool = 0
    #                     w.redbool = 1
    #                     self._right_rotate(w)
    #                     w = x.parent.rightchild
    #                 w.redbool = x.parent.redbool
    #                 x.parent.redbool = 0
    #                 w.rightchild.redbool = 0
    #                 self._left_rotate(x.parent)
    #                 x = x.parent if x.parent is not None else self.root  # 更新根节点
    #         else:
    #             w = x.parent.leftchild
    #             if w.redbool == 1:
    #                 w.redbool = 0
    #                 x.parent.redbool = 1
    #                 self._right_rotate(x.parent)
    #                 w = x.parent.leftchild
    #             if w.rightchild.redbool == 0 and w.leftchild.redbool == 0:
    #                 w.redbool = 1
    #                 x = x.parent
    #             else:
    #                 if w.leftchild.redbool == 0:
    #                     w.rightchild.redbool = 0
    #                     w.redbool = 1
    #                     self._left_rotate(w)
    #                     w = x.parent.leftchild
    #                 w.redbool = x.parent.redbool
    #                 x.parent.redbool = 0
    #                 w.leftchild.redbool = 0
    #                 self._right_rotate(x.parent)
    #                 x = x.parent if x.parent is not None else self.root  # 更新根节点
    #     if x is not None:
    #         x.redbool = 0

    #     if self.root is not None:
    #         self.root.redbool = 0

    
    def delete(self, key):
        node_to_delete = self.search(key)
        if node_to_delete == self.nil:
            return

        # 实际删除的节点
        if node_to_delete.leftchild != self.nil and node_to_delete.rightchild != self.nil:
            successor = self._find_successor(node_to_delete)
            node_to_delete.key, node_to_delete.value = successor.key, successor.value
            node_to_delete = successor

        child = node_to_delete.leftchild if node_to_delete.leftchild != self.nil else node_to_delete.rightchild
        self._transplant(node_to_delete, child)

        if node_to_delete.redbool == 0:
            self._delete_fixup(child)

    def _find_successor(self, node):
        successor = node.rightchild
        while successor.leftchild != self.nil:
            successor = successor.leftchild
        return successor

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.leftchild:
            u.parent.leftchild = v
        else:
            u.parent.rightchild = v
        v.parent = u.parent

    def _delete_fixup(self, x):
        while x != self.root and x.redbool == 0:
            if x == x.parent.leftchild:
                sibling = x.parent.rightchild
                if sibling.redbool:
                    sibling.redbool = 0
                    x.parent.redbool = 1
                    self._left_rotate(x.parent)
                    sibling = x.parent.rightchild
                if sibling.leftchild.redbool == 0 and sibling.rightchild.redbool == 0:
                    sibling.redbool = 1
                    x = x.parent
                else:
                    if sibling.rightchild.redbool == 0:
                        sibling.leftchild.redbool = 0
                        sibling.redbool = 1
                        self._right_rotate(sibling)
                        sibling = x.parent.rightchild
                    sibling.redbool = x.parent.redbool
                    x.parent.redbool = 0
                    sibling.rightchild.redbool = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.leftchild
                if sibling.redbool:
                    sibling.redbool = 0
                    x.parent.redbool = 1
                    self._right_rotate(x.parent)
                    sibling = x.parent.leftchild
                if sibling.rightchild.redbool == 0 and sibling.leftchild.redbool == 0:
                    sibling.redbool = 1
                    x = x.parent
                else:
                    if sibling.leftchild.redbool == 0:
                        sibling.rightchild.redbool = 0
                        sibling.redbool = 1
                        self._left_rotate(sibling)
                        sibling = x.parent.leftchild
                    sibling.redbool = x.parent.redbool
                    x.parent.redbool = 0
                    sibling.leftchild.redbool = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.redbool = 0

    

    def searchByRange(self,node,start, end):
        
        if node !=self.nil:
            self.searchByRange(node.leftchild,start, end)
            if start <= node.key <= end:
                self.result+=node.key+' '+node.value+'\n'
            self.searchByRange(node.rightchild, start, end)
            

