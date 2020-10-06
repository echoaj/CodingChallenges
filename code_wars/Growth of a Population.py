#codewars.com

def nb_year(p0, percent, aug, p):
    years = total = 0
    while True:
        total = p0 + (p0 * percent * 0.01) + aug
        years = years + 1
        if total >= p:
            return years
        p0 = total

print(nb_year(1000, 2, 50, 1200))

'''
def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year
    '''