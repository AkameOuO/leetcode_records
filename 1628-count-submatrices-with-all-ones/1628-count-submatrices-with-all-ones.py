class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        mat2 = []
        for row in mat:
            row2 = []
            cur = 0
            for num in row:
                cur = (cur + 1) * num
                row2.append(cur)
            mat2.append(row2)
        mat2 = list(map(list, zip(*mat2)))

        res = 0
        for row in mat2:
            stack = []
            for i, c in enumerate(row):
                if c == 0:
                    stack = []
                    continue
                
                stack.append([c, i - 1])
                while len(stack) > 1:
                    if stack[-2][0] < c:
                        break
                    stack[-2][0] = c
                    stack.pop()

                for sc, si in stack[::-1]:
                    res += sc * (i - si)
                    i = si

        return res
                
                    