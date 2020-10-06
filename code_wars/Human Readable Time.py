#codewars.com

def make_readable(seconds):
    # Do something
    remainder = hour = minute = 0

    if seconds >= 3600:
        hour = int(seconds / 3600)
        seconds = seconds % 3600

    if seconds >= 60:
        minute = int(seconds / 60)
        seconds = seconds % 60

    if hour < 10:
        string = '0' + str(hour) + ':'
    else:
        string = str(hour) + ':'
    if minute < 10:
        string = string + '0' + str(minute) + ':'
    else:
        string = string + str(minute) + ':'
    if seconds < 10:
        string = string + '0' + str(seconds)
    else:
        string = string + str(seconds)

    return string

print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(43234))

'''
print()
def make_readables(seconds):
    h = seconds / 60 ** 2
    m = (seconds % 60 ** 2) / 60
    s = (seconds % 60 ** 2 % 60)
    return "%02d:%02d:%02d" % (h, m, s)

print(make_readables(0))
print(make_readables(5))
print(make_readables(60))
print(make_readables(43234))'''