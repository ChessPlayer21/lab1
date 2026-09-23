"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    count_vowels_2 = 0
    for i in range(len(text)):
        if text[i] in "euioa":
            count_vowels_2 += 1
        else:
            continue
    return count_vowels_2

        


def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    array_unique_simbols = []
    for i in range(len(text)):
        if text[i] in array_unique_simbols:
            return False
        else:
            array_unique_simbols.append(text[i])
    return True


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    count_bits = []
    while(number > 0):
        count_bits.append(number % 2)
        number = number // 2
    return count_bits.count(1)


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    raise NotImplementedError  # TODO


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    raise NotImplementedError  # TODO


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    raise NotImplementedError  # TODO


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    raise NotImplementedError  # TODO


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    raise NotImplementedError  # TODO
