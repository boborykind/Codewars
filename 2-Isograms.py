def is_isogram(s):
    if not s:
        return True

    letters = set()

    for char in s:
        if char.lower() in letters:
            return False
        letters.add(char.lower())

    return True


user_input = input("Введите слово: ")
print(is_isogram(user_input))
