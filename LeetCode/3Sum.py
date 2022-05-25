# LeetCode 15
# Medium
# O(n^2) solution

# Needs Work
def tsum(array):
    array.sort()
    i = 0
    j = len(array)-1
    results =[]

    while i < j:

        for k in range(i+1, j):
            if array[i] + array[j] + array[k] == 0:
                nums = [array[i], array[j], array[k]]
                if nums not in results:
                    results.append(nums)

        if 0 - array[i] > array[j] - 0:
            i += 1
        else:
            j -= 1

    return results


print(tsum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))