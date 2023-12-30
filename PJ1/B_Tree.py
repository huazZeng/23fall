class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree
        self.result=''
    def searchByEng(self,node,key):
        node,index=self.search(key,self.root)
        if node==None:
            return key+'  NO SUCH WORD'
        return node.keys[index][1]

    def insert(self, k):
        node,_=self.search(k[0],self.root)
        if node!=None:
            #print('allready in')
            return 0
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def search(self, k, x=None):
        
        if x is None:
            x = self.root
        i = 0

    
        while i < len(x.keys) and k > x.keys[i][0] :
            
            i += 1
        if i < len(x.keys) and k== x.keys[i][0] :
            
            return x,i
        elif x.leaf:
            return None,None
        else:
            
            return self.search(k, x.children[i])

    def print_tree(self, x=None, l=0):
        if x is None:
            x = self.root
        print("Level", l, ":", len(x.keys), end=" ")
        print("Keys:", x.keys)
        if len(x.children) > 0:
            l += 1
            for child in x.children:
                self.print_tree(child, l)

    def delete(self, k):
        self._delete(self.root, k)

    def _delete(self, x, k):
        if x is None:
            return
        i = 0
        while i < len(x.keys) and k > x.keys[i][0]:
            i += 1

        if i < len(x.keys) and k == x.keys[i][0]:
            if x.leaf:
                del x.keys[i]
            else:
                pred = self._get_predecessor(x, i)
                x.keys[i] = pred
                self._delete(x.children[i], pred[0])
        else:
            if x.leaf:
                #print(f"Key {k} not found in the B-tree.")
                return
            if i < len(x.keys)+1 and len(x.children) > i:
                if len(x.children[i].keys) < self.t:
                    self._fill_child(x, i)
        
                if len(x.children)==i:
                    i-=1
                self._delete(x.children[i], k)
            
    def searchByRange(self, x, range_start, range_end):
        i = 0
        while i < len(x.keys) and range_start > x.keys[i][0]:
            i += 1

        if x.leaf:
            while i < len(x.keys) and range_start <= x.keys[i][0] <= range_end:
                self.result+=x.keys[i][0]+' '+x.keys[i][1]+'\n'

                i += 1
        else:
            while i < len(x.keys) and x.keys[i][0] <= range_end:
                self.searchByRange(x.children[i], range_start, range_end)
                i += 1

            # Check the rightmost child if it exists
            if i < len(x.children):
                self.searchByRange(x.children[i], range_start, range_end)

    def _get_predecessor(self, x, i):
        current = x.children[i]
        while not current.leaf:
            current = current.children[-1]
        return current.keys[-1]

    def _fill_child(self, x, i):
        if i > 0 and len(x.children[i - 1].keys) >= self.t:
            self._borrow_from_prev(x, i)
        elif i < len(x.children) - 1 and len(x.children[i + 1].keys) >= self.t:
            self._borrow_from_next(x, i)
        elif i > 0:
            self._merge_children(x, i - 1)
        else:
            self._merge_children(x, i)

    def _borrow_from_prev(self, x, i):
        child = x.children[i]
        sibling = x.children[i - 1]

        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()

        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def _borrow_from_next(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]

        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)

        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def _merge_children(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]

        child.keys.append(x.keys.pop(i))
        child.keys.extend(sibling.keys)

        if not child.leaf:
            child.children.extend(sibling.children)

        del x.children[i + 1]

    def preorder_traversal(self, x,level):
        if x is not None:
            self.result+= 'level ='+str(level)+'  child:'+str(len(x.children))
            for key in x.keys:
                self.result+='\\'+key[0]
            self.result +='\n'
            level+=1
            for child in x.children:
                self.preorder_traversal(child,level)
  