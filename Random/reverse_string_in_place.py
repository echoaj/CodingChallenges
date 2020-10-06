#leet code


word = ["h","e","l","l","o"]


def reverse_word(word) -> None:
    front = 0
    back = len(word) - 1

    while front < back:
        temp1 = word[front]
        temp2 = word[back]
        word[back] = temp1
        word[front] = temp2
        front += 1
        back -= 1

reverse_word(word)
print(word)