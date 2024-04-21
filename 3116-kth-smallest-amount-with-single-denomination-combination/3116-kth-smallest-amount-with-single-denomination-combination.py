class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if 1 in coins:
            return k
        
        def cal(n):
            nonlocal coins
            res = 0
            for i in range(len(coins)):
                for l in combinations(coins,i+1):
                    s = 1
                    for c in l:
                        s = math.lcm(s,c)
                    if i % 2 == 0:
                        res += n//s
                    else:
                        res -= n//s
            return res
                    
            for i in range(len(coins)):
                s = 1
                for j in range(i, len(coins)):
                    s = math.lcm(coins[j],s)
                    if (j-i) % 2 == 0:
                        res += n//s
                    else:
                        res -= n//s
                    print(i,j,s,res)
                print(res)
            print(coins,n,res)
            return res
        coins.sort()
        # l = []
        # for c in coins:
        #     for n in l:
        #         if c % n == 0:
        #             break
        #     else:
        #         l.append(c)
        # coins = l
        
        r = 1
        l = 10**12
        while r < l:
            m = (r+l)//2
            if cal(m) < k:
                r = m + 1
            else:
                l = m
        return r