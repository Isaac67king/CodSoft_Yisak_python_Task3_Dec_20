from random import random

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
special_char = "!@$%&*(){}?"
number_char = "0123456789"


def strong_pass(length):
    if length < 8:
        length = 8

    potential_chars = upper_letters + lower_letters + special_char + number_char
    answer = ''
    index = int(random() * len(potential_chars))
    indices = [index]
    while len(indices) < length:
        index = int(random() * len(potential_chars))
        if (index != item for item in indices):
            indices.append(index)

    for i in range(length):
        ch = potential_chars[indices[i]]
        answer += ch
    return answer


def weak_pass(length):
    if length < 4:
        length = 4

    potential_chars = lower_letters + number_char
    password = ''
    index = int(random() * len(potential_chars))
    indices = [index]
    while len(indices) < length:
        index = int(random() * len(potential_chars))
        if (index != item for item in indices):
            indices.append(index)

    for i in range(length):
        ch = potential_chars[indices[i]]
        password += ch

    return password
