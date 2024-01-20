class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(l:=len(matrix[0])):
                matrix[i][j] += min(matrix[i-1][max(0,j-1):(min(j+2,l))])
        return min(matrix[-1])