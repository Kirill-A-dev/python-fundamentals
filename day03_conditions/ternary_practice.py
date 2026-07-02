def is_divisible_by_3(number):
    return "кратно 3" if number % 3 == 0 else "не кратно 3"


def bool_to_string(number):
    return "True" if number == 1 else "False"


def next_second(second):
    return 0 if second == 59 else second + 1


def is_palindrome(word):
    word = word.lower()
    return "палиндром" if word == word[::-1] else "не палиндром"


print(is_divisible_by_3(9))
print(bool_to_string(1))
print(next_second(59))
print(is_palindrome("Казак"))