class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        oppo = 1
        if len(v2) < len(v1):
            v1, v2 = v2, v1
            oppo = -1
        
        v1 += [0] * (len(v2) - len(v1))
        for a, b in zip(v1, v2):
            if int(a) < int(b):
                return -1 * oppo
            elif int(a) > int(b):
                return 1 * oppo
        return 0
                
