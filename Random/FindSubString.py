





def findSubString(string, item):
    item_len = len(item)-1
    index = 0;
    for i in string:
        if i == item[index]:
            if index == item_len:
                return True
            index += 1
        else:
            index = 0
    return False


print(findSubString("I love trading bitcoin.", "bit"))
# Also


print("bit" in "I love trading bitcoin.")
print([4,5] in [9,5,2,6,4,5,8,6,7])