# Find the first non repeating letter in a character

str = "GeeksForGeeks"
dict = {}


for i in str:
    if i not in dict:
        dict.update({i:1})
    else:
        count = dict[i]
        count += 1
        dict.update({i: count})

for i in dict:
    if dict[i] == 1:
        print(i)
        break