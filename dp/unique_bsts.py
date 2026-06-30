'''Unique binary search tree for number n as parameter'''


class Solution:
    def numTrees(self, n: int) -> int:
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        return math.floor(factorial(2 * n) / (factorial(n) * factorial(n + 1)))