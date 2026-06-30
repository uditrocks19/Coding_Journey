# https://www.hackerrank.com/challenges/three-month-preparation-kit-stockmax/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-nine


def stockmax(prices):
    # Write your code here
    n = len(prices)
    mx = [0] * n
    mx[n-1] = 0
    for i in range(n-2, -1, -1):
        mx[i] = max(mx[i+1], prices[i+1])

    tot_sum = 0
    for i in range(n):
        if mx[i] > prices[i]:
            tot_sum += mx[i] - prices[i]

    return tot_sum
