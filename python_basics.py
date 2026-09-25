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
    counter = 0
    number = data.value
    while(number >= 10):
        number = new_number(number)
        counter += 1
    return counter

def new_number(number):
    array_number = []
    string_number = str(number)
    new_number = 1
    for i in range(len(string_number)):
        array_number.append(string_number[i])
    for i in range(len(array_number)):
        new_number = new_number * int(array_number[i])
    return new_number

def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    sum = 0.0
    for i in range(len(predicted)):
        sum = sum + (predicted[i] - expected[i])**2
    return sum / len(predicted)

def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    number_2 = number
    count_number = {}
    while number != 1:
        for i in range(2, number + 1):          
            if number % i == 0:
                if str(i) in count_number:
                    count_number[str(i)] += 1
                else:
                    count_number[str(i)] = 1    
                number = number // i            
                break
            else:
                continue
        else:
            count_number[str(number)] = count_number.get(str(number), 0) + 1
            break                              
    itog_string = ""
    for i in range(1, number_2 + 1):           
        key = str(i)
        if key not in count_number:         
            continue
        if count_number[key] == 0:
            continue
        elif count_number[key] == 1:
            itog_string += f"({key})"
        elif count_number[key] > 1:            
            itog_string += f"({key}**{count_number[key]})"
    return itog_string

def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    if cube_count == 0:
        return 0
    cube_number = 1
    while(cube_count > 0):
        cube_count = cube_count - cube_number**2
        if cube_count == 0:
            return cube_number
        elif cube_count < 0:
            return "It is impossible"
        cube_number += 1
    return cube_number



def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    raise NotImplementedError  # TODO

