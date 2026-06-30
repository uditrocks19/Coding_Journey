from collections import defaultdict

def total_subarray(nums, k):
    l = r = 0
    n = len(nums)
    mp = defaultdict(int)
    tot = 0
    distinct = 0
    for r in range(n):
        mp[nums[r]] +=1
        if mp[nums[r]] == 1:
            distinct +=1

        while distinct > k:
            mp[nums[l]] -=1
            if mp[nums[l]] == 0:
                distinct -=1
            l +=1

        tot += (r - l  + 1)

    return  tot




arr = [1, 2, 1]
print(total_subarray(arr, 2) - total_subarray(arr, 1))
