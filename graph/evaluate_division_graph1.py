'''evaluate division'''

from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            adj[a][b] = value
            adj[b][a] = 1 / value

        def bfs(start, end):
            if start not in adj or end not in adj:
                return -1

            if start == end:
                return 1.0
            vis = set()
            q = deque([(start, 1.0)])
            while q:
                current, product = q.popleft()
                if current == end:
                    return product
                vis.add(current)
                for neighbour, val in adj[current].items():
                    if neighbour not in vis:
                        q.append((neighbour, product * val))
                    if neighbour == end:
                        return product * val

            return -1.0

        res = []
        for a, b in queries:
            res.append(bfs(a, b))
        return res