
# create a function that returns true if there exists a subarray that adds up to a target
# input: array, target
# output: boolean

def subarray_adds_up_to_target(arr, target):
    i = 0
    j = 1
    total = arr[i] + arr[j]
    while j < len(arr):
        if total == target:
            return True
        elif total < target:
            j += 1
            if j < len(arr):
                total += arr[j]
        elif total > target:
            total -= arr[i]
            i += 1
    return False


if __name__ == '__main__':
    result = subarray_adds_up_to_target([1, 2, 3, 4, 5], 9) # True
    print(result)