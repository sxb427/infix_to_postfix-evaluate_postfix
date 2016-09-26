#l=['1','+','2','*','(','3','+','4',')']
#'1-(2^3)*(4+5/(2^6-7))'
string = str(raw_input('enter expression'))
def get(s):
    l=[]
    operators_and_brackets = ['+','-','*','/','^','(',')']
    q=''
    for i in s:
            if i in operators_and_brackets and q!='':
                l.append(q)
                l.append(i)
                q=''
            elif i in operators_and_brackets and q=='':
                l.append(i)
            else:
                q=q+i
    l.append(q)
    if '' in l:
        l.remove('')
    return l
def infix_to_postfix(ex):
    expression = get(ex)
    operators_priority = {'-':1,'+':1,'*':2,'/':2,'^':3}
    stack = []
    postfix = []
    error = 0
    for i in expression:
        if i in operators_priority:
            try:
                while operators_priority[stack[-1]]>=operators_priority[i]:
                    postfix.append(stack[-1])
                    del stack[-1]
            except:
                pass
            finally:
                stack.append(i)
        elif i==')':
            try:
                while stack[-1]!='(':
                    postfix.append(stack[-1])
                    del stack[-1]
            except:
                error = error + 1
                print "ERROR"
                break
            finally:
                del stack[-1]
        elif i=='(':
            stack.append(i)
        else:
            postfix.append(i)
    if '(' in stack or ')' in stack:
        error = error+1
    for i in stack[::-1]:
        postfix.append(i)
    if error>0:
        pass
    else:
        return postfix
def evaluate(postfix):
    operators = ['-','+','*','/','^']
    stack = []
    for i in postfix:
        if i in operators:
            if i=='-':
                result = float(stack[-2]) - float(stack[-1])
                del stack[-1]
                del stack[-1]
                stack.append(result)
            elif i=='+':
                result = float(stack[-2]) + float(stack[-1])
                del stack[-1]
                del stack[-1]
                stack.append(result)
            elif i=='*':
                result = float(stack[-2])*float(stack[-1])
                del stack[-1]
                del stack[-1]
                stack.append(result)
            elif i=='/':
                result = float(stack[-2])/float(stack[-1])
                del stack[-1]
                del stack[-1]
                stack.append(result)
            elif i=='^':
                result = float(stack[-2])**float(stack[-1])
                del stack[-1]
                del stack[-1]
                stack.append(result)
        else:
            stack.append(i)
    if len(stack)!=1:
        print "ERROR"
    else:
        return stack[0]
print "infix expression is",infix_to_postfix(string)
print "answer is",evaluate(infix_to_postfix(string))
        
        
        
        

