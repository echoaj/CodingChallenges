


def containsNearbyDuplicate(nums, k):
    dist = k + 1
    map = {}

    for i in range(len(nums)):
        digit = nums[i]
        if digit in map:
            dist = min(dist, abs(i - map[digit]))

        map[digit] = i

    return True if dist <= k else False


print(containsNearbyDuplicate([1,0,1,1], 1))