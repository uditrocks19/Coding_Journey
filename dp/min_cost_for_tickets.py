'''leetcode 983'''


class Solution:
    def mincostTickets(self, days, costs):
        dp = [0] * 366
        travel_days = set(days)

        for day in range(1, 366):
            if day not in travel_days:
                dp[day] = dp[day - 1]
            else:
                cost_1_day = dp[day - 1] + costs[0]
                cost_7_day = dp[max(0, day - 7)] + costs[1]
                cost_30_day = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(cost_1_day, cost_7_day, cost_30_day)

        return dp[365]