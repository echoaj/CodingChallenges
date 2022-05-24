# codewars.com


def expanded_form(num):
    count = 1
    expanded = " "
    while num > 10:
        expanded = "0" * count + " + " +str(num % 10) + expanded
        num //= 10
        count += 1
    expanded = str(num % 10) + expanded
    return expanded


print(expanded_form(2745))
