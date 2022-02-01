

# return a list of all numbers that when multiplied
def mult_combos(limit, x, y, combos):
    # print(x,y)
    if x > limit:
        return combos
    if y > limit:
        return
    if x*y == limit and [x,y] not in combos:
        combos.append([x,y])
        return
    mult_combos(limit, x, y+1, combos)
    return mult_combos(limit, x+1, y, combos)


print(mult_combos(12, 0, 0, []))
