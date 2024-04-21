class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        for ch in word:
            if "A" <= ch <= "Z":
                if ch.lower() in word:
                    s.add(ch.lower())
            else:
                if ch.upper() in word:
                    s.add(ch)
        return len(s)