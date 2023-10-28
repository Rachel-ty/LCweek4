class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        cnt=0
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            elif not stack:
                cnt+=1
            elif c==')' and stack[-1]=='(' or c==']' and stack[-1]=='[' or c=='}' and stack[-1]=='{':
                stack.pop()
            elif c==')' and stack[-1]!='(' or c==']' and stack[-1]!='[' or c=='}' and stack[-1]!='{':
                stack.pop()
                cnt+=1
        cnt+=len(stack)
        return cnt