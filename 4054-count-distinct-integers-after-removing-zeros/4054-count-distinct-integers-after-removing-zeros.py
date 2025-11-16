class Solution:
    def countDistinct(self, n: int) -> int:
        result = 0
        for i in range(1, 16):
            if n >= 10 ** i:
                result += 9 ** i
            else:
                s = str(n)
                for j, c in enumerate(s):
                    i -= 1
                    c = int(c)
                    if c == 0:
                        break
                    if c == 1:
                        continue
                    result += (c-1) * 9 ** i
                else:
                    result += 1
                break

        return result
                    

