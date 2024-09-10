def square_digits(num):
    num_str = str(num)

    result = ""

    for digit in num_str:
        digit_square = int(digit) * int(digit)

        result += str(digit_square)

    integer_number = int(result)

    return integer_number


num = input("Введите число: ")
print(square_digits(num))
