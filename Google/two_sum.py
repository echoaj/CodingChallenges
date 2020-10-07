


# Step 1: check if compliment in map
# Step 2: if not, store current NUM AS KEY : INDEX AS VALUE
# Step 3: if so, print indaex in dictionary and current index


def two_sum(array, target):
    map = {}

    for i in range(len(array)):
        compliment = target - array[i]
        if compliment not in map:
            map[array[i]] = i
        else:
            print(map[compliment], i)

    print(map)


# Index: 0  1  2  3  4  5  6  7  8
two_sum([1, 0, 4, 2, 5, 6, 3, 6, 7], 9)

