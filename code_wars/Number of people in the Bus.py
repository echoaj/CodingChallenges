#codewars.com

def number(bus_stops):
    # Good Luck!
    total = 0
    for i in bus_stops:
        total = total+ i[0] - i[1]
    return total

print(number([[10,0],[3,5],[5,8]]))
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))



def numbers(stops):
    return sum(i - o for i, o in stops)

print(numbers([[10,0],[3,5],[5,8]]))
print(numbers([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
print(numbers([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))