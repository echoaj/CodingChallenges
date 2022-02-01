

def gcf(x, y, i):
    if x % i == 0 and y % i == 0:
        return i

    return gcf(x, y, i-1)


num1 = 50
num2 = 15
result = gcf(num1, num2, min(num1, num2))
print(result)
