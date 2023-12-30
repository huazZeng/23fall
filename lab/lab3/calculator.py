from stack import stack
class calculator():
    def __init__(self):
        self.inputstr=""
        self.output=0
        self._stack=stack()
        self.Arithmetic_symbols=["+","-","*","/","%"]


    def yourinput(self,Notation):
        self.inputstr=Notation


    def calculate(self):
        elements = self.inputstr.split(' ')
        for element in elements:
            if element in self.Arithmetic_symbols:
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.push(self.perform_operation(element,a,b))
                
            else :
                self._stack.push(int(element))
                
        return self._stack.pop()

    def perform_operation(self,operator, operand2, operand1):
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
