class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        for s in sandwiches:
            if c[s] == 0:
                return c[s^1]
            c[s] -= 1
        return 0