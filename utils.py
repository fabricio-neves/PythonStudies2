def find_max(numbers):
    maximum = 0
    for number in numbers:
        if maximum < number:
            maximum = number
    return maximum

