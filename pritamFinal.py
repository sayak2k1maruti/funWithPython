listOfNumber  =   ['1','2','3','4','5','6','7','8','9','0']
listofOperator = ['+','-','*','/','^']

def doMath(lists):
    a=0.0
    b=0.0
    c = ' '
    fraction = 0
    stage = 1
    count = 1
    for i in lists:
        if stage == 1:
            if i in listOfNumber:
                if fraction == 0:
                    a = a*10 + float(i)
                elif fraction == 1:
                    a = a + float(i*(10**(-count)))
                    count+=1
                else:
                    continue
            elif i == '.':
                fraction = 1
                count = 1
            elif i in listofOperator:
                c = i
                count = 1
                stage = 2
                fraction = 0
            else:
                print("Incorrect Input")
        if stage == 2:
            if i in listOfNumber:
                if fraction == 0:
                    b = b*10 + float(i)
                elif fraction == 1:
                    b = b + float(i*(10**(-count)))
                    count+=1
            elif i == '.':
                fraction = 1
                count = 1
            
    
    if c == '+':
        return a+b
    elif c == '-':
        return a-b
    elif c == '*':
        return a*b
    elif c == '/':
        if b!=0:
            return a/b
        else:
            print("Cannot divide by 0")
            return 0
    elif c == '^':
        return a**b


inputs = input()
string = list(inputs)
for i in string:
    if i == " ":
        string.remove(i)   #removing all spaces

print(doMath(string))