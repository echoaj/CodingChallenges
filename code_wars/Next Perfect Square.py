#codewars.com

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    num = sq **0.5
    if num.is_integer():
        return (num + 1)**2
    else:
        return -1


print(find_next_square(121))
print(find_next_square(15241383936))
print(find_next_square(299))