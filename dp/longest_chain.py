class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key=lambda x: x[0])
        lis = [1] * n
        if n <= 1:
            return 1

        for i in range(1, n):
            c, d = pairs[i][0], pairs[i][1]
            for j in range(i):
                a, b = pairs[j][0], pairs[j][1]
                if c > b and lis[i] < lis[j] + 1:
                    lis[i] = max(lis[i], lis[j] + 1)

        return max(lis)