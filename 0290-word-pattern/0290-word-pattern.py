class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False 
        d = {}
        for x in range(len(words)):
            if pattern[x] not in d:
                if words[x] in d.values():
                    return False
                d[pattern[x]] = words[x]
            else:
                if d[pattern[x]] != words[x]:
                    return False
        return True