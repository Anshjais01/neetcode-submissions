class Solution:
    def hasDuplicate(self, x):
        return len(x)!=len(set(x))