n = int(input())
from collections import deque

arr = deque(list(range(1, n + 1)))
res = []
s = 1

while arr:
    if s % 2 == 0:
        res.append(arr.popleft())
    else:
        arr.append(arr.popleft())
    s += 1

print(*res)