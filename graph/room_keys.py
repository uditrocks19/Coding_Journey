'''Is it possible to visit all rooms'''
# https://leetcode.com/problems/keys-and-rooms/description/
from collections import defaultdict, deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = defaultdict(list)
        n = len(rooms)
        for i, keys in enumerate(rooms):
                for key in keys:
                    adj[i].append(key)

        q = deque()
        vis = set()
        q.append(0)
        while q:
            x = q.popleft()
            vis.add(x)
            for room in adj[x]:
                if room not in vis:
                    q.append(room)

        for i in range(n):
            if i not in vis:
                return False

        return True
