class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            res=[]
            for i in s:
                if i !="#":
                    res.append(i)
                elif res:
                    res.pop()
            return "".join(res)
        return build(s) == build(t)