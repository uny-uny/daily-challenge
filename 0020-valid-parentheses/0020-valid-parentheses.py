class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={'(':')', '{':'}','[':']'}
        for i in s:
            if i not in mapping:
                if not stack or mapping[stack.pop()]!=i:
                    return False
            else:
                stack.append(i)
        return len(stack)==0