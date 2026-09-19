class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        for ch in s:
            if ch=="(":
                lst.append(")")
            elif ch=="[":
                lst.append("]")
            elif ch=="{":
                lst.append("}")
            elif not lst or lst.pop()!=ch:
                return False
        return len(lst)==0

        