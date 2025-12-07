def valid_parentheses(str):
    if len(str) % 2 !=0:
        return False
    
    stack = []
    closing = ""
    for i in str:
        if i in ["(", "[" , "{"]:
            stack.append(i)
            closing = ""
        if i in[")" ,"]" ,"}"]:
            closing = i
            if closing == ")":
                closing = "("
            elif closing == "]":
                closing = "["
            elif closing == "}":
                closing = "{"

        
            if stack and stack[len(stack)-1] == closing:
                stack.pop()
            else:
                return False

    if len(stack) == 0:      
        return True
    
    return False





print(valid_parentheses("([])"))
