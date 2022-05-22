

def sorter(lst):
    first = lst.pop(0)
    str = " ".join(lst)
    lst.insert(0, first)
    return str

def sortBoxes(boxList):
    oldBoxes = []
    newBoxes = []
    for box in boxList:
        tokens = box.split()
        second = tokens[1][0]
        if second.isalpha():
            oldBoxes.append(tokens)
        else:
            newBoxes.append(tokens)
    oldBoxes.sort(key=sorter)
    newBoxes.sort(key=sorter)
    total = []
    for lst in oldBoxes:
        total.append(" ".join(lst))
    for lst in newBoxes:
        total.append(" ".join(lst))
    return total

inpt = ["ykc 82 01",
        "eo first qpx",
        "09z cat hamster",
        "06f 12 25"]

print(sortBoxes(inpt))