import re

def HTMLElements(strParam):
    elementList = re.findall(r'<(./*[a-z]*)>', strParam)

    stack = []    
    for elem in elementList:
        if stack and stack[-1] == elem:
            stack.pop()
        
        else:
            stack.append('/' + elem)
        
    if not stack:
        return 'true'

    return stack[len(stack)//2-1][1:]

# keep this function call here 
print(HTMLElements("<div><div><b></b></div></p>"))
print(HTMLElements("<div>abc</div><p><em><i>test test test</b></em></p>"))