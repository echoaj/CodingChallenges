
'''
Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If method gets number, it should return string.

Examples:

to_underscore('TestController')         # returns test_controller
to_underscore('MoviesAndBooks')         # returns movies_and_books
to_underscore('App7Test')               # returns app7_test
to_underscore(1)                        # returns "1"
'''


def to_underscore(camel):
    if isinstance(camel, str):
        camel_list = list(camel)
        start = len(camel_list)-1

        for i in range(start, 0, -1):
            if camel_list[i].isupper():
                camel_list.insert(i, '_')

        camel = ''.join(camel_list).lower()
        print(camel)
    else:
        print(str(camel))


to_underscore('MoviesAndBooks')