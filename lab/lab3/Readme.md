#Lab 3
##Code
###Infix to Postfix
``` python
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
        #使用字符串切割获取每个元素子串
        elementSequence=self.inputStr.split()

        for element in elementSequence:
            #判断元素是否为运算符号 对括号进行特殊处理 其余比较后，正常压栈
            if element in self.Arithmetic_symbols:
                
                if element==")":
                        while self._stack.peek()!="(":
                            if self._stack.is_empty() :
                                print("Math  error ")
                                return
                
                            result+=str(self._stack.pop())
                        self._stack.pop()
                else :
                    #栈为空则直接压入
                    if self._stack.is_empty() :
                        self._stack.push(element)
                    else:
                        #比较优先级
                        while(self.prioritytable[self.Arithmetic_symbols.index(self._stack.peek())][self.Arithmetic_symbols.index(element)]):
                            result+=str(self._stack.pop())+" "
                            if  self._stack.is_empty() :
                                break
                        self._stack.push(element)
            else:
                #如果是字符或者数字子串 直接进入结果
                result+=element+" "
        while not self._stack.is_empty():
            result+=str(self._stack.pop())+" "

        return result        

```
###calculator
``` python
def __init__(self):
        self.inputstr=""
        self.output=0
        self._stack=stack()
        self.Arithmetic_symbols=["+","-","*","/","%"]


    def yourinput(self,Notation):
        self.inputstr=Notation


    def calculate(self):
        #遇到数字压栈 遇到字符弹出操作数 运算后返回栈
        elements = self.inputstr.split(' ')
        for element in elements:
            if element in self.Arithmetic_symbols:
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.push(self.perform_operation(element,a,b))
                
            else :
                self._stack.push(int(element))
                
        return self._stack.pop()
#计算函数 简化calculate函数
    def perform_operation(self,operator, operand1, operand2):
        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                return "除数不能为零"
            result = (int)(operand1 / operand2)
        elif operator == "%":
            if operand2 == 0:
                return "取余的除数不能为零"
            result = operand1 % operand2
        else:
            return "无效的运算符"
        
        return result

```
##Answer
###calculate
Postfix : 3 5 + 2 7 * /
Result : 0

Postfix : 25 5 + 3 * 21 7 / 1 + -
Result : 86

Postfix : 5 1 2 + 4 * + 3 - 7 4 5 - + +
Result : 20

Postfix : 36 3 / 5 + 2 * 14 - 3 * 24 2 / 1 - + 2 /
Result : 35

Postfix : 20 4 - 2 * 14 + 7 / 1 - 5 * 9 + 12 3 / 2 + -
Result : 28

Postfix : 10 5 + 2 * 8 - 4 / 3 + 6 * 12 2 * 4 + - 18 3 / 2 * + 5 -
Result : 27

Postfix : 24 3 / 6 + 2 * 14 - 2 / 5 + 4 * 16 2 * 3 + - 21 3 / 2 * +
Result : 27

Postfix : 20 6 + 2 * 14 - 7 / 1 + 4 * 10 2 * 3 + - 27 3 / 2 * + 4 -
Result : 15

Postfix : 8 4 + 3 * 18 - 2 / 7 + 5 * 10 - 2 + 4 * 12 - 6 + 2 * 3 - 2 /
Result : 280

###Infix to Postfix
Infix : ( A + B ) * C
Postfix : A B +C * 

Infix : A + ( B - C )
Postfix : A B C -+ 

Infix : A * ( B + C ) / D
Postfix : A B C +* D / 

Infix : ( A + B ) * ( C - D )
Postfix : A B +C D -* 

Infix : A + B * C - D / E
Postfix : A B C * + D E / - 

Infix : ( A * B ) + ( C / D ) - E
Postfix : A B *C D /+ E - 

Infix : ( A + B ) / ( C + D ) * E
Postfix : A B +C D +/ E * 

Infix : A * ( B + C ) - ( D * E )
Postfix : A B C +* D E *- 

Infix : ( A + B ) * ( C - D ) / ( E + F )
Postfix : A B +C D -* E F +/ 

Infix : A * ( B + ( C * ( D - ( E / ( F + ( G * H ) ) ) ) ) ) / I
Postfix : A B C D E F G H *+/-*+* I / 

