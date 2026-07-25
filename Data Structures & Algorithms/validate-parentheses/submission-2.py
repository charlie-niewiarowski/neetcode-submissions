class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        
        stack = []
        for i in range (len(s)):
            stack.append(s[i])

            if stack[-1] in closed and i > 0:
                if stack[len(stack) - 2] in opened and opened.index(stack[len(stack) - 2]) == closed.index(stack[-1]):
                    a, b = stack.pop(), stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
            
        return False
