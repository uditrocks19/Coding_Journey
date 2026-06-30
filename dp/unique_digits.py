class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        if n == 0:
            return 1
        ans = 1
        for k in range(1, n + 1):
            z = 9
            for j in range(1, k):
                z = z * (10 - j)
            ans += z
        return ans