def reverse_string(string):
    index = len(string) - 1
    reversed_string = ''

    while index >= 0:
        current_char = string[index]
        reversed_string = reversed_string + current_char
        # То же самое через интерполяцию
        # reversed_string = f'{reversed_string}{current_char}'
        index = index - 1

    return reversed_string

print(reverse_string('Game Of Thrones'))

