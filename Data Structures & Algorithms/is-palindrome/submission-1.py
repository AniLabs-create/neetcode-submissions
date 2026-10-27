import string

TABLE: dict[int, None] = {ord(c): None for c in string.whitespace + string.punctuation}


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned: str = s.translate(TABLE).lower()
        return cleaned == cleaned[::-1]

