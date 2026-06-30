n = int(input())
coins = list(map(int, input().split()))

coins.sort()

reachable = 0

for coin in coins:
    if coin > reachable + 1:
        print(reachable + 1)
        break
    reachable += coin
else:
    print(reachable + 1)