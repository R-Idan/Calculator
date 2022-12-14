import operator

inp = input("Enter your equation: ")
stack = []
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
    global stack
    operatorStack = []
    operatorStack.append('#')
    isNumber=False
    count=0
    #convert negative numbers from -number to _number for calculation later
    isEligible=True
    for i in inp:
        if i!='-':
            isEligible=False
        elif count+1<len(inp)and (inp[count+1]=='+' or inp[count+1]=='/' or inp[count+1]=='*' or inp[count+1]=='-'):
            isEligible=False
        if count==0 or inp[count-1]=='(' or inp[count-1]=='+' or inp[count-1]=='/' or inp[count-1]=='*' or inp[count-1]=='-':
            if isEligible==True:
                inp = inp[:count] + '_' + inp[count+1:]
        isEligible=True
        count=count+1
    count=0
    for i in inp:
        if i.isnumeric()==True or i=='.' or i=='_':
            if(isNumber==True):
                stack[len(stack)-1]+=i
            else:
                stack+=i
                isNumber=True
        elif i=='(':
            operatorStack.append('(')
            isNumber=False
        elif i ==')':
            while(operatorStack[-1]!='#' and operatorStack[-1] != '('):
                stack.append(operatorStack[-1])
                operatorStack.pop()
            operatorStack.pop()
            isNumber=False
        else:
            if preced(i)>preced(operatorStack[-1]):
                operatorStack.append(i)
                isNumber=False
            else:
                while operatorStack[-1]!='#' and preced(i)<= preced(operatorStack[-1]):
                    stack.append(operatorStack[-1])
                    operatorStack.pop()
                operatorStack.append(i)
                isNumber=False

        count=count+1
    while(operatorStack[-1]!='#'):
        stack.append(operatorStack[-1])
        operatorStack.pop()

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#try to check for bad input
try:
    GetPostFix(inp)
    numStack = []
    for i in range(len(stack)):
        stack[i]=stack[i].replace('_','-')

    #calculate with the postfix equation
    for i in range(len(stack)):
        if stack[i].isnumeric()==True or isfloat(stack[i])==True or (stack[i][0]=='-' and stack[i][1:].isnumeric()==True) :
            numStack.append(float(stack[i]))
        else:
            a=numStack.pop()
            b=numStack.pop()
            numStack.append(allowed_operators[stack[i]](b,a))
            
    num = numStack[-1]
    if num % 1 == 0:
        print(int(numStack[-1]))
    else:
        print(numStack[-1])
except:
    print("bad input")