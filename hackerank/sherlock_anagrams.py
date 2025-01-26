# https://www.hackerrank.com/challenges/three-month-preparation-kit-sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-eight

from collections import defaultdict
def sherlockAndAnagrams(s):
    # Write your code here
    adj = defaultdict(int)
    n = len(s)
    for i in range(n):
        for j in range(i+1, n + 1):
            x = "".join(sorted(s[i:j]))
            adj[x] +=1

    arr = [(x*(x-1))//2 for x in list(adj.values())]
    return sum(arr)
