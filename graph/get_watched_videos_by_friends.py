'''get watched videos by your friends'''
# https://leetcode.com/problems/get-watched-videos-by-your-friends/

from collections import defaultdict, deque
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # Adjacency list (not needed as `friends` is already an adjacency list)
        n = len(friends)
        vis = set()  # To track visited nodes
        q = deque([id])  # BFS queue starting with the given person
        vis.add(id)

        # BFS to find friends at the specified level
        while level > 0:
            for _ in range(len(q)):  # Process one BFS level
                person = q.popleft()
                for friend in friends[person]:
                    if friend not in vis:
                        vis.add(friend)
                        q.append(friend)
            level -= 1

        # Collect videos watched by friends at the specified level
        video_count = defaultdict(int)
        while q:
            person = q.popleft()
            for video in watchedVideos[person]:
                video_count[video] += 1

        # Sort videos by frequency and then alphabetically
        result = sorted(video_count.items(), key=lambda x: (x[1], x[0]))
        return [video for video, _ in result]
