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

# dynamic programming approach

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans