
def lengthLongestPath(input: str) -> int:
    largest = 0
    stack = [0]
    array = input.split("\n")

    for i in range(len(array)):
        level = array[i].count("\t")
        path = len(array[i]) - level

        # Assumption is that if the level is less
        # than the stack length, we are at a parent directory
        while level < len(stack)-1:
            stack.pop()

        if "." in array[i]:
            largest = max(largest, path+stack[-1])  #compare previous largest path to current
        else:
            stack.append(stack[-1]+path+1)

    return largest


answer = lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" )
print(answer)



dir = """dir\n
            \tsubdir1\n
                \t\tfile1.ext\n
                \t\tsubsubdir1\n
            \tsubdir2\n
                \t\tsubsubdir2\n
                    \t\t\tfile2.ext"""