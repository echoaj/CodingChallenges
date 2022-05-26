

array = [1, 8, 6, 2, 5, 4, 8, 3, 7]

x = 0
y = len(array)-1
largest = 0

while x != y:
    left = array[x]
    right = array[y]
    area = min(left, right) * (y-x)
    largest = max(largest, area)
    if left <= right:
        x += 1
    else:
        y -= 1

print(largest)
