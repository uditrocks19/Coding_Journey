class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        tot_bit = math.floor(math.log(n, 2))
        res = []
        for j in range(0, n + 1):
            ans = 0
            for k in range(0, tot_bit + 1):
                if (j & 1 << k):
                    ans += 1
            res.append(ans)
        return res