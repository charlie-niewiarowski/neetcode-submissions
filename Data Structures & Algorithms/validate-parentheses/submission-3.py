class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        stack = []
        for c in s:
            if c in closedToOpen:
                if stack and closedToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
