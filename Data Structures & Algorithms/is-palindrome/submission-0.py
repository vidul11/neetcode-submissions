class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            # skip non-alphanumeric on the left
            while start < end and not s[start].isalnum():
                start += 1
            # skip non-alphanumeric on the right
            while start < end and not s[end].isalnum():
                end -=1
            # now compare
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True