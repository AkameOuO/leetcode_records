class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s1 = 0
        s2 = 0
        last = -1
        last2 = -1
        res = 0
        for i, fruit in enumerate(fruits):
            # print(f"{i} {fruit}|s1:{s1} {last}|s2:{s2} {last2}|{res}")
            if fruit != last:
                if fruit != last2:
                    res = max(res, i - s2)
                    # print(res, i, s2)
                    s2 = s1
                if last2 != last:
                    last2 = last
                s1 = i
                last = fruit
        l = len(fruits)
        return max(res, l - s2)
            