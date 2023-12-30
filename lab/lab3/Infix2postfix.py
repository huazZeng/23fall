from stack import stack
class Infix2postfix:
    def __init__(self):
        self.inputStr=""
        self.output=""
        self._stack=stack()
        self.prioritytable=[[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,1,1,0,0,0],[1,1,1,1,0,0,0],[1,1,1,1,1,0,0],[0,0,0,0,0,0,1],[1,1,1,1,1,1,0]]
        self.Arithmetic_symbols=["+","-","*","/","%","(",")"]
    def yourinput(self,infix):
        self.inputStr=infix
    
    def conversion(self):
        elementSequence=[]
        result=""
        elementSequence=self.inputStr.split()

        for element in elementSequence:
            if element in self.Arithmetic_symbols:
                
                if element==")":
                        while self._stack.peek()!="(":
                            if self._stack.is_empty() :
                                print("Math  error ")
                                return
                
                            result+=str(self._stack.pop())
                        self._stack.pop()
                else :
                    if self._stack.is_empty() :
                        self._stack.push(element)
                    else:
                        while(self.prioritytable[self.Arithmetic_symbols.index(self._stack.peek())][self.Arithmetic_symbols.index(element)]):
                            result+=str(self._stack.pop())+" "
                            if  self._stack.is_empty() :
                                break
                        self._stack.push(element)
            else:
                result+=element+" "
        while not self._stack.is_empty():
            result+=str(self._stack.pop())+" "

        return result        
