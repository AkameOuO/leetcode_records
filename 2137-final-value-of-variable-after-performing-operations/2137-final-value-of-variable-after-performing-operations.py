class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return ((c := reduce(lambda x,y:x+y,map(Counter, operations)))["+"] - c["-"]) // 2