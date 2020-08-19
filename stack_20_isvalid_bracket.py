class Solution:
    def isValid_v1(self, s: str) -> bool:
        if not s: return True

        def isPair(c, stack):
            if not stack: return False
            if (c==')' and stack[-1]=='(') or\
               (c==']' and stack[-1]=='[') or\
               (c=='}' and stack[-1]=='{'):
                stack.pop()
                return True
            else:
                return False
            
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in [')', ']', '}']:
                if not isPair(c, stack):
                    return False

        return True if not stack else False
    
    def isValid(self, s):
        if not s: return True
        if s.find("{}")!=-1 or s.find("[]")!=-1 or s.find("()")!=-1:
            s = s.replace("{}","").replace("[]","").replace("()","")
            return self.isValid(s)
        else:
            return False