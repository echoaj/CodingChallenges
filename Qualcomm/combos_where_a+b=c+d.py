
combos = {}


# Given a list of numbers find all combinations where a+b=c+d
nums = [1, 7, 3, 8, 12, 4, 2, 0, 5, 10]
# 7+3=8+2
# 7+1=8+0

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        key = nums[i] + nums[j]
        if key not in combos:
            combos[key] = [(nums[i], nums[j])]
        else:
            combos[key].append((nums[i], nums[j]))

print(combos)
for key in combos:
    if len(combos[key]) > 1:
        for i in range(len(combos[key])):
            pair = combos[key][i]
            string = f"{pair[0]} + {pair[1]}"
            for j in range(i+1, len(combos[key])):
                pair2 = combos[key][j]
                string2 = f" = {pair2[0]} + {pair2[1]}"
                print(string + string2)

