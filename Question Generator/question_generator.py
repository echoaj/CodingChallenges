from random import*


def generator(lst):
    for i in lst:
        yield i

nf = []
normal_file = open('questions','r')
for i in normal_file:
    nf.append(i)

ga = []
ga_file = open('GA_questions','r')
for i in ga_file:
    ga.append(i)

vs = []
vs_file = open('Viasat_questions','r')
for i in vs_file:
    vs.append(i)


total = nf + ga + vs

shuffle(nf)
shuffle(ga)
shuffle(vs)
shuffle(total)

###################
study = total
###################

gen = generator(study)

for i in range(len(study)):
    print(next(gen))
    input()



normal_file.close()
ga_file.close()
vs_file.close()