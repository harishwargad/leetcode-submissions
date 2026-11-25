class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain_word = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if plain_word == plain_word[::-1]:
            return True
        else:
            return False