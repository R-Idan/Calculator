import operator

inp = input("Enter your equation: ")
#Operators allowed
allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}
    
#how important is the operator
def preced(ch):
    if(ch == '+' or ch == '-'):
        return 1
    elif(ch == '*' or ch == '/'):
        return 2
    else:
        return 0
#convert from normal equations(infix) to postfix for calculation
def GetPostFix(inp):
    operatorStack = []
    operatorStack.append('#')
    outStr=""

    for i in inp:
        if i.isnumeric()==True: 
            outStr+=i
        elif i=='(':
            operatorStack.append('(')
        elif i ==')':
            while(operatorStack[-1]!='#' and operatorStack[-1] != '('):
                outStr += operatorStack[-1]
                operatorStack.pop()
            operatorStack.pop()
        else:
            
            if preced(i)>preced(operatorStack[-1]):
                operatorStack.append(i)
            else:
                while operatorStack[-1]!='#' and preced(i)<= preced(operatorStack[-1]):
                    outStr+=operatorStack[-1]
                    operatorStack.pop()
                operatorStack.append(i)
    while(operatorStack[-1]!='#'):
        outStr+=operatorStack[-1]
        operatorStack.pop()
    return outStr

#try to check for bad input
try:
    postFixEquation = GetPostFix(inp)
    numStack = []
    #calculate with the postfix equation
    for i in postFixEquation:
        if i.isnumeric()==True:
            numStack.append(int(i))
        else:
            a=numStack.pop()
            b=numStack.pop()
            numStack.append(allowed_operators[i](b,a))
except:
    print("bad input")
finally:
    print(numStack[-1])
