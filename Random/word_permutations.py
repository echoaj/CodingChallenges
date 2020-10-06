from itertools import permutations
name = permutations("alex")
name = list(name)
perm = []

for i in name:
    print(i)
print(len(name))