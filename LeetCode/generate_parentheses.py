# generate parentheses perumation

def generate_parentheses(string, left, right, n):
    if len(string) == n*2:
        print(string)
        return
    if left < n:
        generate_parentheses(string + '(', left + 1, right, n)
    if right < left:
        generate_parentheses(string + ')', left, right + 1, n)


def genpar(n):
    generate_parentheses("", 0, 0, n)

genpar(3)