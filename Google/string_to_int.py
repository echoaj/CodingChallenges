'''
Hey all, I recieved a question called "String to Int" in an interview,
and I was flabberghasted at how simple it sounded at first, but difficult it is in practice.

Turn a string to a number

Example 1:

Input: "Three hundred million"
Output: 300,000,000
Example 2:

Input: "Five Hundred Thousand"
Output: 500,000
'''


ones = {"one":1, "two":2, "three":3, "four":4, "five":5,
        "six":6, "seven":7, "eight":8, "nine":9}

tens = {"ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty":80, "ninety":90}

hundreds = {"hundred":100, "thousand":1000, "million":1000000, "billion":1000000000}

words = "three hundred million fifty nine"
'''     3 * 100 * 1000000   +   50  +  9     '''

words = "fifty nine thousand six hundred twelve"
words = "fifty nine thousand sixty two"

num_string = words.split()

print(words)

num_list = []
for w in num_string:
    if w in ones:
        num_list.append(ones[w])
    elif w in tens:
        num_list.append(tens[w])
    elif w in hundreds:
        num_list.append(hundreds[w])


print(num_list)

stack = num_list.copy()
stack.reverse()
print(stack)


while len(stack) != 1:
    x = stack[-1]
    stack.pop()
    y = stack[-1]
    stack.pop()

    if x < y:
        stack.append(x * y)
    else:
        stack.append(x + y)
    print(stack)










