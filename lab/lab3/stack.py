class stack:
    #初始化
    def __init__(self):
        self.stack = []
    
    #进出栈操作
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if(len(self.stack)<1):
            print("stack is empty")
        else:
            return self.stack.pop()
    
    #检查栈操作
    def size(self):
        return len(self.stack)

    def is_empty(self):
        return  len(self.stack)<1

    def peek(self):
        if(len(self.stack)<1):
            print("stack is empty")
        else:
            return self.stack[-1]

    