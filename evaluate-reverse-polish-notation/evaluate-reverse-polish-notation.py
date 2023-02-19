class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for chr in tokens:
            try:
                chr=int(chr)
            except:
                op1=str(stack.pop())
                op2=str(float(stack.pop()))
                operation=op2+chr+op1
                res=int(eval(operation))
                stack.append(res)
            else:
                stack.append(chr)
        temp=stack.pop()
        return temp
