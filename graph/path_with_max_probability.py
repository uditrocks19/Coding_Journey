'''path with max probability'''
# https://leetcode.com/problems/path-with-maximum-probability/description/
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create adjacency list with the probabilities
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            a, b = edge[0], edge[1]
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))

        # Max heap to store (-probability, node), we use negative probability to simulate a max-heap
        q = []
        # Distance array to track max probability to each node
        dis = [0.0 for _ in range(n)]

        # Start with the start_node with probability 1.0
        heapq.heappush(q, (-1.0, start_node))
        dis[start_node] = 1.0

        # Perform a modified Dijkstra's algorithm
        while q:
            prob, node = heapq.heappop(q)
            prob = -prob  # Revert back to positive probability

            # If we have already found a better probability, continue
            if prob < dis[node]:
                continue

            # Explore neighbors
            for neighbor, edge_prob in adj[node]:
                new_prob = prob * edge_prob
                if new_prob > dis[neighbor]:
                    dis[neighbor] = new_prob
                    heapq.heappush(q, (-new_prob, neighbor))

        # Return the result for the end_node, rounded to 5 decimal places
        return round(dis[end_node], 5) if dis[end_node] > 0 else 0

