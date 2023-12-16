class Solution:
    def entityParser(self, text: str) -> str:
        table = {
            "&quot;": "\"",
            "&apos;": "'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
            "&amp;": "&"
        }
        for k,v in table.items():
            text = text.replace(k,v)
        return text