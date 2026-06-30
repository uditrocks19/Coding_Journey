# https://leetcode.com/problems/knight-probability-in-chessboard/description/
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # lets define a dp witgh
                directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
                dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
                dp[0][row][column] = 1
                for moves in range(k):
                    for i in range(n):
                        for j in range(n):
                            if dp[moves][i][j] > 0:
                                for d in directions:
                                    x1 = i + d[0]
                                    y1 = j + d[1]
                                    if (x1 >=0 and x1<n) and (y1 >=0 and y1<n):
                                        dp[moves + 1][x1][y1] += dp[moves][i][j]/8.0

                tot_prob = 0
                for i in range(n):
                    for j in range(n):
                        tot_prob += dp[k][i][j]

                return tot_prob
