class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        def set_bits(n):
            cnt = 0
            for i in range(0, 32):
                if (n & 1 << i):
                    cnt += 1

            return cnt

        mn = float('inf')
        ans = 0
        for i in range(0, 10 ** 9 + 1):
            if set_bits(i) == set_bits(num2):
                if (i ^ num1) < mn:
                    mn = (i ^ num1)
                    ans = i

        return ans

https://selfcare.actcorp.in/home


