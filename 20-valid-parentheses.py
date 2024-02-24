def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

    for c in s:
        # if we get closing parentheses
        if c in closeToOpen: 
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
            
        # if we get opening parentheses
        else: 
            stack.append(c)

    return True if not stack else False
    

