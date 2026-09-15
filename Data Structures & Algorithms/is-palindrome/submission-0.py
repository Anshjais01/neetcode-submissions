class Solution:
    def isPalindrome(self, s: str) -> bool:
        j="".join(char.lower() for char in s if char.isalnum())
        return j==j[::-1]