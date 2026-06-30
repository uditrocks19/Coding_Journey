'''Network delay Time '''
# https://leetcode.com/problems/network-delay-time/description/

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = []
        dis = [float('inf')] * (n + 1)  # Distance list with 1-based indexing
        adj = defaultdict(list)

        # Build the adjacency list
        for a, b, c in times:
            adj[a].append((b, c))

        # Start with the source node k
        heapq.heappush(q, (0, k))
        dis[k] = 0  # The distance to the source node is 0

        while q:
            curr_d, node = heapq.heappop(q)

            # If the current distance is already greater than the best distance, skip processing
            if curr_d > dis[node]:
                continue

            # Explore neighbors
            for neighbor, time in adj[node]:
                new_dist = curr_d + time
                if new_dist < dis[neighbor]:  # Only update if we found a shorter path
                    dis[neighbor] = new_dist
                    heapq.heappush(q, (new_dist, neighbor))

        # The answer is the maximum distance, but if there's any node that is unreachable,
        # return -1 (in the case where we still have infinity distances).
        max_distance = max(dis[1:])
        return max_distance if max_distance < float('inf') else -1
