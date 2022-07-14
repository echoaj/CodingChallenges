

# given a list of unique numbers, return all combinations where a+b=c+d
# time complexity O(n^4)
def abcd(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                for l in range(k+1, len(nums)):
                    if nums[i] + nums[j] == nums[k] + nums[l]:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
    return result


cache = {}
def abcd_2(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            pair = (nums[i], nums[j])
            pair2 = (nums[j], nums[i])
            sum_ = sum(pair)
            if sum_ in cache:
                # if pair not in cache[sum_] and pair2 not in cache[sum_]:
                cache[sum_].append(pair)
            else:
                cache[sum_] = [pair]

    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum_ = sum([nums[i], nums[j]])
            if sum_ in cache:
                for pair in cache[sum_]:
                    if pair[0] != nums[i] and pair[1] != nums[j]:
                        result.append(f"{nums[i]} + {nums[j]} = {pair[0]} + {pair[1]}")

    return result


array = [1, 2, 7, 4, 5, 14, 3, 10, 9]
for result in abcd_2(array):
    print(result)