class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 :
            return True
        
        s_ = "".join(char for char in s if char.isalnum()).lower()

        return s_ == s_[::-1]



        