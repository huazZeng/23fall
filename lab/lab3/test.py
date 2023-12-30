from  Infix2postfix import  Infix2postfix
from calculator import calculator
import re
conversion=Infix2postfix()
calculator=calculator()
with open("lab3\\answer.txt",'w') as savedfile:

    file_path = "lab3\code 02 test.txt"
    with open(file_path, 'r') as file:
        # 读取文件中的所有数据
        text1 = file.read()
        
    pattern = r'\((\w+)\): ([\d\s+*/\-]+)\n'
    matches = re.findall(pattern, text1)
    # 输出匹配到的表达式
    for match in matches:
        name, expression = match
        calculator.yourinput(expression)
        savedfile.write("Postfix : "+expression+"\n"+"Result : "+str(calculator.calculate())+"\n\n")

    file_path = "lab3\code 01 test.txt"
    with open(file_path, 'r') as file:

        lines = file.readlines()
    for line in lines:
    
        line = line.strip()
        conversion.yourinput(line)
        savedfile.write("Infix : "+line+"\n"+"Postfix : "+conversion.conversion()+"\n\n")
        
