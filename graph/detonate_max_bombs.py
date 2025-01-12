'''detonate max bombs'''

# https://leetcode.com/problems/detonate-the-maximum-bombs/description

from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # Function to check if bomb `j` is in the range of bomb `i`
        def check(x1, y1, r, x2, y2):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r ** 2

        # BFS function to count detonated bombs starting from a given index
        def bfs(adj, index):
            vis = set()  # Visited set for indices
            q = deque([index])  # Start BFS from the given index
            vis.add(index)
            cnt = 1

            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if neighbor not in vis:
                        vis.add(neighbor)
                        q.append(neighbor)
                        cnt += 1

            return cnt

        # Build adjacency list
        adj = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if check(bombs[i][0], bombs[i][1], bombs[i][2], bombs[j][0], bombs[j][1]):
                        adj[i].append(j)

        # Find the maximum number of bombs that can be detonated
        mx = 0
        for i in range(n):
            mx = max(mx, bfs(adj, i))

        return mx

