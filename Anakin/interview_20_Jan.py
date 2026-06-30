class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def check(s1, s2):
            n, m = len(s1), len(s2)
            if abs(m - n) >= 2:
                return False
            for i in range(m):
                x = s2[:i] + s2[i + 1:]
                if x == s1:
                    return True

            return False

        n = len(words)
        words = sorted(words, key=lambda x: len(x))
        if n == 1:
            return 1
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])

        return


